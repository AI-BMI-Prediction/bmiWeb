from django.shortcuts import render
import torch
import torch.nn as nn
import numpy as np

# Create your views here.

def index(request):
    #GET 
    if request.method =='GET':
        return render(request, 'index.html')
    
    #POST에서 값 불러오기
    elif request.method =='POST':
        #String 에서 float으로 불러오기
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        step_count = float(request.POST['step_count'])
        calorie_intake =float( request.POST['calorie_intake'])
        burned_calorie = float(request.POST['burned_calorie'])
        sleep = float(request.POST['sleep'])
        if(height==0):
            bmi=0
        else:
            bmi= weight/(height*height/100)

        # Tensor화 시킬 데이터 리스트에 넣기
        input = []
        input.append(weight)
        input.append(step_count)
        input.append(burned_calorie)
        input.append(calorie_intake)
        input.append(sleep)
        input.append(height)

        #Model 구조
        class DNNModel(nn.Module):
            def __init__(self):
                super(DNNModel, self).__init__()
                self.input_layer = nn.Linear(6, 128)
                self.hidden_layer1 = nn.Linear(128, 256)
                self.hidden_layer2 = nn.Linear(256, 128)
                self.output_layer = nn.Linear(128, 3)
                self.relu = nn.ReLU()

            def forward(self, x):
                out = self.relu(self.input_layer(x))
                out = self.relu(self.hidden_layer1(out))
                out = self.relu(self.hidden_layer2(out))
                out = self.output_layer(out)
                return out
        
        #Model 선언
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        model = DNNModel()  # Model 생성
        model.eval()

        #input 값들 Tensor화 시키기
        inputs = torch.FloatTensor(input)

        #모델 로드
        model.load_state_dict(torch.load('C:\\Users\\user\\Desktop\\project\\bmiWeb\\bmiproject\\home\\static\\DNNModel.pth'))

        #예측 값
        output = model(inputs)
        _, outputs=output.max(dim=-1)
        predict=outputs.numpy()
        
        if(predict==0):
            str3="BMI가 유지한다"
        elif(predict==1):
            str3="BMI가 증가한다"
        elif(predict==2):
            str3="BMI가 감소한다"
        else:
            str3="예측실패"

        if predict==0 and bmi <15:
            str= "BMI가 유지될 것으로 예측됩니다."
            str2= "사용자는 저체중이라서 몸무게를 더 찌우시는 것이 건강에 더 좋아 보입니다."
        elif predict==0 and bmi<25 and bmi>15:
            str= "BMI가 유지될 것으로 예측됩니다."
            str2= "사용자는 정상체중이라서 몸무게를 더 유지하시는 것이 건강에 더 좋아 보입니다."
        elif predict==0 and bmi>25:
            str= "BMI가 유지될 것으로 예측됩니다."
            str2= "사용자는 과체중이라서 몸무게를 더 감량하시는 것이 건강에 더 좋아 보입니다."
        if predict==1 and bmi <15:
            str= "BMI가 증가될 것으로 예측됩니다."
            str2= "사용자는 저체중이라서 몸무게를 더 찌우시는 것이 건강에 더 좋아 보입니다."
        elif predict==1 and bmi<25  and bmi>15:
            str= "BMI가 증가될 것으로 예측됩니다."
            str2= "사용자는 정상체중이라서 몸무게를 더 유지하시는 것이 건강에 더 좋아 보입니다."
        elif predict==1 and bmi>25:
            str= "BMI가 증가될 것으로 예측됩니다."
            str2= "사용자는 과체중이라서 몸무게를 더 감량하시는 것이 건강에 더 좋아 보입니다."
        if predict==2 and bmi <15:
            str= "BMI가 감소할 것으로 예측됩니다."
            str2= "사용자는 저체중이라서 몸무게를 더 찌우시는 것이 건강에 더 좋아 보입니다."
        elif predict==1 and bmi<25  and bmi>15:
            str= "BMI가 감소할 것으로 예측됩니다."
            str2= "사용자는 정상체중이라서 몸무게를 더 유지하시는 것이 건강에 더 좋아 보입니다."
        elif predict==1 and bmi>25:
            str= "BMI가 감소할 것으로 예측됩니다."
            str2= "사용자는 과체중이라서 몸무게를 더 감량하시는 것이 건강에 더 좋아 보입니다."


    return render(request, 'index.html', {'outputs':str3,'str':str,'str2':str2})


