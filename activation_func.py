'''
    1. 딥러닝(Depp Learning)
        1) 여러 층(특히 은닉층이 여러 개)을 가진 인공신경망을 사용하여 머신 러닝을 수행하는 것
        - 입력층 : 학습하고자 하는 데이터를 입력 받음.
        - 은닉층 : 모든 입력 노드로부터 입력값을 받아 가중합을 계산하고, 이 값을 활성화 함수에 적용하여 출력층에 전달
        - 출력층 : 최종 결과 출력
        - 가중치 : 입력 신호가 출력에 미치는 영향을 조절하는 매개변수로, 입력값의 중요도를 결정
        - 편향 : 가중합에 더하는 상수로, 하나의 뉴런에서 활성화 함수를 거쳐 최종적으로 출력되는 값을 조절


        2) 다중 퍼셉트론(MLP, multilayer perceptron)
            - 입력층과 출력층 사이에 은닉층(hidden layer)을 가지고 있는 퍼셉트론

        3) 활성화 함수 (activation function)
            - 입력 신호가 출력 결과에 미치는 영향도를 조절하는 매개변수
            - 활성화 함수를 사용하는 이유
                - 출력값을 0~1 (-1-1) 사이의 값으로 변환해야 하는 경우에 사용
                - 비선형(Non-linear)을 위해 사용
                    - 직선이 아닌, 그래프에서 곡선 모양을 취하는 것

            - 종류
                - 계산 함수
                    - 입력 신호의 총합이 0을 넘으면 1을 출력하고, 그렇지 않으면 0을 출력하는 함수
                - 시그모이드(sigmoid) 함수
                    - x값의 변화에 따라 0에서 1까지의 값을 출력하는 s자형 함수
                    - 로지스틱 함수라고도 부름
                - 하이퍼블릭 탄젠트 (Hyperbolic Tangent) 함수
                    - 시그모이드 함수와 유사
                    - -1 ~ 1의 값을 가지면서 데이터 평균이 0이라는 점이 다름
                - 렐루(ReLU) 함수
                    - x가 음의 값을 가지면 0을 출력하고, 양의 값을 가지면 x를 그대로 출력
                    - max(0, x)로 계산이 간단하여 학습 속도가 매우 빠르다.

'''

import numpy as np
import matplotlib.pyplot as plt


def step(x):
    result = x > 0.00000001                      # 부동소수점 오차 방지, Ture 또는 False
    return result.astype(int)                    # 정수로 변환

x = np.arange(-10.0, 10.0, 0.1)
y = step(x)
plt.plot(x, y)
#plt.show()

print("---------------------------------------------------------------")



def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-10.0, 10.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
#plt.show()

print("---------------------------------------------------------------")

x = np.linspace(-np.pi, np.pi, 60)  # 지정된 구간 내에서 균일한 간격으로 수를 가지는 배열을 반환함.
#print(x)
y = np.tanh(x)
plt.plot(x, y)
#plt.show()

print("---------------------------------------------------------------")


def relu(x):
    return np.maximum(x, 0)

x = np.arange(-10.0, 10.0, 0.1)
# print(x)
y - relu(x)
plt.plot(x, y)
plt.show()