from data.user import User
from pages.registration_page import RegistrationPage

FILE = 'test.png'


def test_registration_user(preparations, remove_advertisment):

    alesya = User(
        first_name='Alesya',
        last_name='Family',
        email='vititi5980@vootin.com',
        gender='Female',
        mobile_phone='8923456323',
        date_of_birth=('2005', 'April', '18'),
        subjects='English',
        hobbies='Reading',
        upload_file='test.png',
        address='test test',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()

    registration_page.fill_registration_form(alesya)
    registration_page.should_registered_user_with(
        full_name=f'{alesya.first_name} {alesya.last_name}',
        email=alesya.email,
        gender=alesya.gender,
        number=alesya.mobile_phone,
        dateofbirth=f'{alesya.date_of_birth[2]} {alesya.date_of_birth[1]},{alesya.date_of_birth[0]}',
        subjects=alesya.subjects,
        hobbies=alesya.hobbies,
        photo=alesya.upload_file,
        address=alesya.address,
        stateandcity=f'{alesya.state} {alesya.city}'
    )


