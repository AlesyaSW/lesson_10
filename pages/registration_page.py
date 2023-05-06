import os
from selene.support.shared import browser
from selene import be, have


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_mail = browser.element('#userEmail')
        self.gender = browser.element('[for="gender-radio-2"]')
        self.number = browser.element("[id=userNumber]")
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element("[for=hobbies-checkbox-2]")
        self.document = browser.element('#uploadPicture')
        self.address = browser.element("[id=currentAddress]")
        self.state = browser.element("[id=state]")
        self.state_select = browser.element("[id=react-select-3-option-0]")
        self.city = browser.element("[id=city]")
        self.city_select = browser.element("[id=react-select-4-option-0]")
        self.submit = browser.element("[id=submit]")

    def set_first_name(self, first_name):
        self.first_name.should(be.blank).type(first_name)
        return self

    def set_last_name(self, last_name):
        self.last_name.should(be.blank).type(last_name)
        return self

    def set_email_name(self, user_mail):
        self.user_mail.should(be.blank).type(user_mail)
        return self

    def select_gender(self, value):
        self.gender.should(have.text(f'{value}')).click()
        return self

    def fill_number(self, number):
        self.number.should(be.blank).type(number)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(month)
        self.date_of_birth_year.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, english):
        self.subjects_input.type(english).press_enter()
        return self

    def select_hobbies(self, value):
        self.hobbies.should(have.text(value)).click()
        return self

    def upload_document(self, value):
        self.document.send_keys(os.getcwd() + value)
        return self

    def fill_address(self, address):
        self.address.should(be.blank).type(address)
        return self

    def select_state(self, value):
        self.state.click()
        self.state_select.should(have.text(f'{value}')).click()
        return self

    def select_city(self, value):
        self.city.click()
        self.city_select.should(have.text(f'{value}')).click()
        return self

    def submit_click(self):
        self.submit.click()
        return self

    def should_registered_user_with(self, full_name, email, gender, number, dateofbirth, subjects, hobbies, photo,
                                    address, stateandcity):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                dateofbirth,
                subjects,
                hobbies,
                photo,
                address,
                stateandcity,
            )
        )
        return self
