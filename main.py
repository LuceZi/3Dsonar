import plotly.graph_objects as go
import math
import random

# 模擬的角度與距離資料
sim_data = []
for theta in range(0, 180, 10):     # 水平角度
    for phi in range(30, 90, 10):   # 垂直角度
        r = random.uniform(50, 100)  # 隨機距離（假設是 cm）
        sim_data.append((theta, phi, r))

# 轉換為 x, y, z 座標
x_vals, y_vals, z_vals = [], [], []

for theta_deg, phi_deg, r in sim_data:
    theta = math.radians(theta_deg)
    phi = math.radians(phi_deg)
    
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

# 用 plotly 畫圖
fig = go.Figure(data=[go.Scatter3d(
    x=x_vals,
    y=y_vals,
    z=z_vals,
    mode='markers',
    marker=dict(
        size=4,
        color=z_vals,  # 顏色根據 z 值變化
        colorscale='Viridis',
        opacity=0.8
    )
)])

fig.update_layout(
    scene_camera=dict(
        eye=dict(x=0, y=2, z=0)  # 垂直從上往下看
    ),
    scene=dict(
        xaxis=dict(title='X (cm)', range=[-100, 100], dtick=20),
        yaxis=dict(title='Y (cm)', range=[-100, 100], dtick=20),
        zaxis=dict(title='Z (cm)', range=[0, 100], dtick=20),
        bgcolor="black",
    )
)


fig.show()
