from selenium import webdriver
from model import Question
from selenium.common.exceptions import NoSuchElementException


class ProgHab(object):
    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_tests_page()

    def go_to_tests_page(self):
        self.driver.get('https://proghub.ru/tests')
        slide_elms = self.driver.find_elements_by_class_name('testCard')

        for el in slide_elms:
            link = el.find_element_by_tag_name('a')
            me_link = link.get_attribute('href')

            if self.lang in me_link:
                # languen = link.split('/')[-1]
                print(me_link)
                self.driver.get(me_link)
                # btn = self.driver.find_elements_by_class_name('btn btn-block btn-primary')
                # print(btn.text)
                self.driver.get('https://proghub.ru/q/0ep23b06jgf3uy1d')
                break

    def parse_question_page(self):
        question = Question()
        self.find_question_text(question)
        self.find_question_code(question)
        self.find_question_answer(question)

        print(question.text)

    def find_question_text(self, question):
        try:
            question_text_el = self.driver.find_element_by_class_name('title')
            question.text = question_text_el.text
        except NoSuchElementException:
            print('question_text_el not find')

    def find_question_code(self, question):
        try:
            question_code_el = self.driver.find_element_by_tag_name('code')
            question.code = question_code_el.text
        except NoSuchElementException:
            print('question_text_code not find')

    def find_question_answer(self, question):
        try:
            question_answer_el = self.driver.find_elements_by_class_name('answer')
            for el in question_answer_el:
                answers = el.find_element_by_tag_name('span')
                l = [answers.text]
                question.answer = l
                print(l)
        except NoSuchElementException:
            print('question_text_answer not find')


def main():
    driver = webdriver.Chrome('D:\Python\Scripts\chromedriver.exe')
    parse = ProgHab(driver, 'python-oop')
    parse.parse()
    parse.parse_question_page()

    # # btn_el = driver.find_element_by_class_name('btn-cyan btn btn-block btn-promo')
    # # btn_el.click()
    # title_h1 = driver.find_element_by_tag_name('h1')
    # print(title_h1.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
