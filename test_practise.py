import unittest
from tkinter import *

import practise


class TestPractise(unittest.TestCase):
    def test_bubble_sort(self):
        list=[('12', 'simran siris', 'simransiris@gmail.com', '21', 'female', 'Bsc Hons in Ethical Hacking', '345678',
          'ertyui'),
         ('13', 'prativa pun', 'prativapun@gmail.com', '21', 'female', 'Bsc Hons incomputing', '45678', 'ertyui'), (
         '11', 'amantika karki', 'amantikakarki@gmail.com', '20', 'female', 'Bsc Hons in Ethical Hacking', '45678',
         'qwertyu'), (
         '123', 'anisha karki', 'anishakarki@gmail.com', '11', 'female', 'Bsc Hons in Ethical Hacking', '3456',
         'wertyu')]
        exp_result=[('11', 'amantika karki', 'amantikakarki@gmail.com', '20', 'female', 'Bsc Hons in Ethical Hacking', '45678',
          'qwertyu'), (
         '12', 'simran siris', 'simransiris@gmail.com', '21', 'female', 'Bsc Hons in Ethical Hacking', '345678',
         'ertyui'),
         ('13', 'prativa pun', 'prativapun@gmail.com', '21', 'female', 'Bsc Hons incomputing', '45678', 'ertyui'), (
         '123', 'anisha karki', 'anishakarki@gmail.com', '11', 'female', 'Bsc Hons in Ethical Hacking', '3456',
         'wertyu')]
        rootVal = Tk()
        sm = practise.sort(rootVal)
        sm.combo_sort.set("Std_ID")
        sm.combo_sortBy.set("Ascending")
        ac_result=sm.Sort(list)

        print('Sort test')
        print(list)
        print(exp_result)
        print(ac_result)
        self.assertEqual(exp_result, ac_result)

    def test_search(self):
        list = [('12', 'simran siris', 'simransiris@gmail.com', '21', 'female', 'Bsc Hons in Ethical Hacking', '345678', 'ertyui'),
                ('13', 'prativa pun', 'prativapun@gmail.com', '21', 'female', 'Bsc Hons incomputing', '45678', 'ertyui'),
                ('11', 'amantika karki', 'amantikakarki@gmail.com', '20', 'female', 'Bsc Hons in Ethical Hacking', '45678', 'qwertyu'),
                ('123', 'anisha karki', 'anishakarki@gmail.com', '11', 'female', 'Bsc Hons in Ethical Hacking', '3456', 'wertyu')]

        exp_result = [('12', 'simran siris', 'simransiris@gmail.com', '21', 'female', 'Bsc Hons in Ethical Hacking', '345678', 'ertyui')]
        rootVal = Tk()
        sm = practise.StudentManagement(rootVal)
        sm.txt_search.delete(0, 'end')
        sm.txt_search.insert(0, "simran siris")
        ac_result = sm.search(list)
        print('Search test')
        print(list)
        print(exp_result)
        print(ac_result)
        self.assertEqual(exp_result, ac_result)

if __name__=='__main__':
    unittest.main()