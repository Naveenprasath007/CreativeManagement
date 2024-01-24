from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
load_dotenv()
from .models import *


def generate(request):
        if request.method == "POST":
            input=request.POST.get('input')
            result=scriptgenerate(input)
            paragraphs = result.split('\n\n')

            # Print individual paragraphs
            for i, paragraph in enumerate(paragraphs, start=1):
                if i == 1:
                    paragraph1=paragraph
                elif i == 2:
                    paragraph2=paragraph
                elif i == 3:
                    paragraph3=paragraph
                elif i == 4:
                    paragraph4=paragraph
                elif i == 5:
                    paragraph5=paragraph

            scriptdetails=ssScriptdetails(UserID='1',prompt=input,script1=paragraph1,
                                        script2=paragraph2,script3=paragraph3,
                                        script4=paragraph4,script5=paragraph5)
            scriptdetails.save()      
            script={"paragraph1":paragraph1,"paragraph2":paragraph2,"paragraph3":paragraph3,"paragraph4":paragraph4,"paragraph5":paragraph5}
            return render(request,'script_studio/scriptgenerator.html',{'result':result,"script":script})
        else:
            return render(request,'script_studio/scriptgenerator.html')



def scriptgenerate(input):
    number_of_text=5
    openai.api_key = os.getenv('api_key')
    prompt = f"Create a {number_of_text} different content for compelling advertisement for {input} that highlights its unique features and benefits. Emphasize why customers should choose Particular {input} over competitors. Use persuasive language and give the output in one single paragraph for each"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with the topics and create the text content for the topic."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=750,
    )

    result = completion.choices[0].message.content   
    return result



