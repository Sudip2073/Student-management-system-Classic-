import unittest
from Finalcode import*

root = Tk()
a = assignment(root)

class final(unittest.TestCase):
    def test_search(self):

        list = [(1, 'sudip', 'shrestha', 19, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '123456'),
                (2, 'sudip', 'kumar', 29, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '23456684')]
        ex_result = [(1, 'sudip', 'shrestha', 19, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '123456')]

        a.search.set('lname')

        ac_result = a.linear_search(list, 'shrestha')
        self.assertEqual(ac_result, ex_result)

    def test_sorting(self):


        a.sort_by.set('ID')
        a.var.set('Ascending')
        array_test = [(1, 'sudip', 'shrestha', 19, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '123456'),
                (2, 'sudip', 'kumar', 29, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '23456684')]
        ex_result = [(1, 'sudip', 'shrestha', 19, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '123456'),(2, 'sudip', 'kumar', 29, 'Male', 'BSc.(Hons) Ethical Hacking', 'ktm', '23456684')]

        ac_result = a.quick_sort(array_test,0,len(array_test)-1)
        self.assertEqual(ac_result, ex_result)




if __name__=='__main__':
    unittest.main()