import openai
from pydantic import BaseModel

openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
openai.api_key = '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'


class Document(BaseModel):
    item: str = ''


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature= 0.8,
        messages=[
            {"role": "system", "content": """Eres un profesor de programación universotario experto en el desarrollo frontend,
            devuelve una explicacion y ejemplo básico del tema que se te proporciona.
        E.G
        Selectores en CSS
        Son herramientas utilizadas para definir el estilo que se le quiere dar a los elementos CSS
        table{
            border: solid 1px black;
            background-color: blueviolet;
            border-collapse: collapse;
        }
        Donde se le asigna un estilo a los elementos del tipo tabla
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    total_tokens= completion.usage.total_tokens

    print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
    return [response, total_tokens]
