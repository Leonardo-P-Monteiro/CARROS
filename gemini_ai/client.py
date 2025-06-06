from google import genai

def get_car_ai_bio(model, brand, year):
    prompt = f'Crie uma bio com até 800 characteres em tom neutro que apresente\
        e exalte as características do carro do model {model} do ano {year} \
        da marca {brand}. Não precisa mencionar novamente o nome do carro, \
        sua marca e ano.'
    client = genai.Client(api_key='AIzaSyAHaXq_OEmad1LtIE3czUkcSfRDvJUUa9E')
    response = client.models.generate_content(
        model = 'gemini-2.0-flash',
        contents= prompt
    )

    return response.text