
from pages.registration_page import RegistrationPage

FILE = 'test.png'


def test_open(preparations, remove_advertisment):
    registration_page = RegistrationPage()
    registration_page.set_first_name('Alesya'). \
        set_last_name('Family'). \
        set_email_name('vititi5980@vootin.com'). \
        select_gender('Female'). \
        fill_number('8923456323'). \
        fill_date_of_birth('2005', 'April', '18'). \
        fill_subjects('English'). \
        select_hobbies('Reading'). \
        upload_document(f'/resources/{FILE}'). \
        fill_address('test test'). \
        select_state('NCR'). \
        select_city('Delhi'). \
        submit_click(). \
        should_registered_user_with('Alesya Family', 'vititi5980@vootin.com', 'Female', '8923456323',
                                                  '18 April,2005', 'English', 'Reading', 'test.png',
                                                  'test test', 'NCR Delhi')



