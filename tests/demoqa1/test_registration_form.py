from allure_commons.types import Severity
from selene import have, browser, command

import allure


@allure.title('Успешное заполнение формы регистарции')
def test_demoqa(setup_browser):
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Авторизация')
    allure.dynamic.story('Отображение страницы входа')
    allure.dynamic.label('owner', 'PrinceAA')
    allure.dynamic.link(
        'https://testit.pgk.ru/projects/3300/tests/25865?isolatedSection=4ef8f76a-4926-480f-a888-658d75812697',
        name='Авторизация. Отображение страницы входа1',
    )
    with allure.step('Открытие страницы'):
        browser.open('/automation-practice-form')

    with allure.step('Заполнение профиля'):
        browser.element('#firstName').type('Ezekiel')
        browser.element('#lastName').type('Romaguera')
        browser.element('#userEmail').type('fakedata72553@gmail.com')
        browser.element('label[for="gender-radio-1"]').click()

    with allure.step('Заполнение номер телефона'):
        browser.element('#userNumber').type('1234567890')

    with allure.step('Дата рождения'):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select>option[value="1905"]').perform(
            command.js.scroll_into_view
        ).click()
        browser.element('.react-datepicker__month-select>option[value="11"]').perform(
            command.js.scroll_into_view
        ).click()

        browser.element('.react-datepicker__day--014').perform(command.js.click)
        browser.element('#subjectsInput').type('English').press_enter()
        browser.element('#subjectsInput').type('Arts').press_enter()
        browser.element('label[for=hobbies-checkbox-1]').perform(command.js.click)
        browser.element('label[for=hobbies-checkbox-2]').perform(command.js.click)
        browser.element('label[for=hobbies-checkbox-3]').perform(command.js.click)

    with allure.step('Загрузка файла'):
        browser.element('#uploadPicture').send_keys(
            r'C:\Users\ChirkinAA\PycharmProjects\teacher-prince-qa_guru_python_12_jenkins_demoqa\resources\oyboy.jpg'
        )

    with allure.step('Заполнение адреса'):
        browser.element('#currentAddress').type('841 Alvis Union')
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text('Haryana')
        ).click()

        browser.element('#city').click()

        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text('Karnal')
        ).click()
        browser.element('#submit').press_enter()
        browser.element('#submit').perform(command.js.click)

    with allure.step('Проверка заполнения формы'):
        browser.all('.table-responsive .table td:nth-child(2)').should(
            have.exact_texts(
                'Ezekiel Romaguera',
                'fakedata72553@gmail.com',
                'Male',
                '1234567890',
                '14 December,1905',
                'English, Arts',
                'Sports, Reading, Music',
                'oyboy.jpg',
                '841 Alvis Union',
                'Haryana Karnal',
            )
        )

    browser.element('#closeLargeModal').click()
