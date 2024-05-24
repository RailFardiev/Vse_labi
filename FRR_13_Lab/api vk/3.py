import vk_api

def predict_user_age(user_id):
    # Авторизация
    vk_session = vk_api.VkApi(token='vk1.a.ebyGEasoACfresGbZ09Hr9QO0nvbRvPjpYc3OSDLch68h5A2h85K7kGzTBfvIUgwnpjhPnnBlgyq3QGlimg1J-Np2E7_5L8_PqB7vivJFwZTybC_cM_YVZ2WYc9yLFri7ovqa5BCMXyoWdXF6fxm_dLLnHiXwNo9Ctrobc2hHgALqKGo41Ma6_6AfFCaLDbu54v4LJZujmR10Bq8pgWL6w')
    #vk_session = vk_api.VkApi(token='vk1.a.NUqQvIkAL0Dm_ZBXJopBdcWPZgPQoKkmkCfyG46WTIk09CJiri0_zgakWwjb1s6XZHvELdMKTAowDPWIAUG7YlHgxiIPXgoDWIdBT4Eeap7l0KM7ln1bLv9dk8Cvxr15UOEIhz0eA4Z6k45mGpm_YqgQj-q_uFo7LHk2FmrUZG_CQAaQ5uj2TFVf02p6P1IlkX2aDN17QCKBFiTX8jSufw&expires')

    vk = vk_session.get_api()
    
    # Получаем информацию о друзьях пользователя
    friends = vk.friends.get(user_id=user_id, fields='bdate')
    
    ages = []
    for friend in friends['items']:
        if 'bdate' in friend:
            bdate = friend['bdate'].split('.')
            if len(bdate) == 3:
                age = 2024 - int(bdate[2])
                ages.append(age)
    
    if len(ages) > 0:
        predicted_age = sum(ages) // len(ages)
        return predicted_age
    else:
        return "Недостаточно данных для прогнозирования возраста"

# Пример использования
user_id = '186287124'
predicted_age = predict_user_age(user_id)
print(f"Прогнозируемый возраст пользователя: {predicted_age}")