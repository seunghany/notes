import torch
import torch.nn as nn

# Step 1) Discriminant 정의
D = nn.Sequential(
    nn.Linear(784, 128), # Input dimension 784, Hidden dimension 128
    nn.ReLU(), # 0 이상이면 출력, 0 이하면 0을 출력
    nn.Linear(128, 1), # Output demension 같은 경우 진짜인지, 가짜인지 알아야 하기 떄문에 Dimension 1로 (0,1)
    nn.Sigmoid()) # Sigmoid 걸어서 D 가 내보낼 수 있는 output range가 [0,1] 사이

# Step 2) Generator 생성
G = nn.Sequential(
    nn.Linear(100, 128), # 입력 값 input 100 dimension 그리고 hidden 128 이라고 가정
    nn.ReLU(),
    nn.Linear(128, 784), # 원본 이미지 생성
    nn.Tanh()
    )

# Step 3) Loss 함수 생성
criterion = nn.BCELoss()  # Binary cross entropy loss function
# supervised learning 에서 많이 사용됨

