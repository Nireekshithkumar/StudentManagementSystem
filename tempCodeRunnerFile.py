if os.path.exists(self._teacher_file):
            with open(self._teacher_file, "r") as handle:
                self._teacherDB = json.load(handle)
        else:
            self._teacherDB = {"principle": "1234"}
            self._save_teacher_db()