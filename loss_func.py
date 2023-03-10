'''
    1. 딥러닝 학습
        1) 순전판(Forward Propagotion)
            - 입력층에서 출력층 방향으로 연산이 진행
        2) 손실 함수(Loss Function)
            - 예측값과 실제값의 차이(오차)를 구하는 함수
                - 두 값의 차이가 클수록 손실함수의 값은 커짐
                - 두 값의 차이가 작을수록 손실함수의 값도 작아짐

            - 신경망에서 학습을 시킬 때는 실제 출력과 원하는 출력 사이의 오차를 이용한다.
              오차를 계산하는 함수를 손실함수라고 함.
            - 신경망에서도 학습의 성과를 나타내는 지표가 있어야 함. 이 손실함수가 해당된다.

            - MSE (Mean squared error)
                - 평균 제곱 오차
                - 예측값과 실제값의 차이의 제곱을 구한 후, 그 값들의 평균을 구하는 것
                - MSE가 작을수록 예측값과 실제값의 차이가 적은 것을 의미함.
                - MSE = 1/n * ∑((predicted_value - actural_val)^2)
'''
import numpy as np

# target : 정답(실제 값), y : 예측 값
def MSE(target, y):
    return np.mean((y - target) ** 2)

y = np.array([0.0, 0.0, 0.8, 0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0])
target = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
print(MSE(target, y))

print("-------------------------------------------------------------------")

y = np.array([0.9, 0.0, 0.8, 0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0])
target = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
print(MSE(target, y))
