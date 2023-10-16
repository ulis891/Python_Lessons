from HW_7_module import file_system as fs


if __name__ == "__main__":
    #   Задачи с семинара
    fs.create_random_num_pair("num.txt", 10)
    fs.name_filler("name.txt", 10)
    fs.join_file("name.txt", "num.txt", "new_join_file.txt")
    fs.file_maker("txt", path="txt_dir")
    fs.ext_maker({"txt": 5, "exe": 2, "csv": 3})
    fs.create_subdir("txt")
    #   Практическое задание
    fs.batch_rename_files("txt_dir", "_new_txt_file", 3, ".ttt", ".txt", [3, 6])
