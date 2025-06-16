from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai
import json

client = openai.OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1",
)

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        try:
            user_message = request.POST.get("prompt", "").strip()

            chat_response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Siz aqlli, sabrli va foydalanuvchining savollariga faqat O'zbek tilida "
                            "aniq, qisqa va tushunarli tarzda javob beradigan sun'iy intellektsiz. "
                            "Faqat siz haqingizdagi savollar (masalan: 'siz kimsiz?', 'sizni kim yaratgan?', 'sizni kim ishlab chiqqan?') bo‘lsa, "
                            "'Men Dadamirzayev Hasanboy tomonidan ishlab chiqilgan sun’iy intellektman. Savollaringiz bo‘lsa, mamnuniyat bilan yordam beraman!' deb javob bering. "
                            "Boshqa barcha savollarga mavzudan chalmay, mantiqiy, to‘g‘ri va tushunarli tarzda qisqacha javob bering. "
                            "Texnik, ilmiy yoki amaliy savollarda aniq izoh bering, kerak bo‘lsa, qisqa misol yoki qadamlar bilan tushuntiring. "
                            "Hech qachon foydalanuvchining savolini mensimang. Har bir murojaatga jiddiy yondashing. "
                            "Yordamchi kabi o‘zingizni tuting, lekin rasmiy va ishonchli bo‘ling."
                        )

                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            reply = chat_response.choices[0].message.content.strip()

            return render(request, 'chat.html', {'response': reply, 'prompt': user_message})

        except Exception as e:
            return render(request, 'chat.html', {'error': str(e)})

    return render(request, 'chat.html')