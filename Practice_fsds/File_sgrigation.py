import re
import shutil
import os
import docx


class Operations:
    @classmethod
    def segregate(cls, src: str) -> str:
        """
        This will segregate the files in the source location in the folder
        :param src: str
        :return: str
        """
        meta_data = {}
        patt_list = []

        for file in os.listdir(src):

            # Rename the file without '_'
            if not ("_" in file) and not (file.endswith(".py")):
                print(file)
                name = re.findall(r"^[A-Za-z][A-Za-z0-9_]+[^_^.]", file)[0]  # Assignment1
                ext = re.findall(r"[.].+", file)[0]  # .docx
                print(name, ext)
                # This will print the output as programming_assignment1 (1).docx
                rename_file = f"Programming_" + name + " (1)" + ext
                os.rename(src=file, dst=rename_file)

        # Rename the duplicate files
        # Replace the () with advanced keyword
        for file in os.listdir(src):
            if not os.path.isdir(file):

                if re.search(r"\(\d\)", file):  # finding (number) inside the '()'
                    rename_file = re.sub(r"\s\(\d\)", "(Advanced)", file)  # SPACE(number) will be renamed to (Advanced)
                    os.rename(src=file, dst=rename_file)
                else:
                    rename_file = file

                # Create the respective folders
                cate = re.findall(r"^[A-Za-z_\(\)]+[^0-9^.^_^\s]", rename_file)[0]

                patt = re.findall(r"[A-Za-z]+[^.]", cate)[0]

                # Create the respective directories
                if not (rename_file.endswith(".py")):
                    if re.search("\(Advanced\)", rename_file):
                        cate += "_Advanced"
                        patt += "_A"
                        meta_data[patt] = cate
                    else:
                        cate += "_Basic"
                        patt += "_B"
                        meta_data[patt] = cate

                    if patt not in patt_list:
                        patt_list.append(patt)
                        os.mkdir(meta_data[patt])
                if not rename_file.endswith(".py"):
                    pass
                shutil.move(src=rename_file, dst=f'.\\{meta_data[patt]}')

    print('All file irrigated Successfully!!')

    @classmethod
    def write_to_file(cls, src, dst, ext):
        """
        This will write all the data of the files in the source location to a single destination file
        :param src:
        :param dst:
        :param ext:
        :return:
        """

        combined = open(dst, "w+", encoding="utf-8")
        for dir_path, dir_name, file_names in os.walk(src):
            for file in file_names:
                if file.endswith(ext):
                    path = os.path.join(dir_path, file)
                    heading = re.findall(r"[A-Za-z_0-9\(\)]+[^.]", file)[0]

                    try:
                        doc = docx.Document(path)
                        data = ""
                        full_text = []
                        combined.writelines(f"\n\n------------{heading}------------\n\n")

                        for para in doc.paragraph:
                            full_text.append(para.text)
                            data = '\n'.join(full_text)

                        combined.write(data)

                    except IOError:
                        print("there was an error opening the file.")
                        return
        combined.close()
        print(f"All the files data copied to {dst}")
