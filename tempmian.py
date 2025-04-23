import plotly.graph_objects as go
import math, random, time
from IPython.display import display
from IPython.display import clear_output

# 初始資料
x_vals, y_vals, z_vals = [], [], []

# 建立空圖
fig = go.FigureWidget()
scatter = go.Scatter3d(
    x=[],
    y=[],
    z=[],
    mode='markers',
    marker=dict(size=4, color=[], colorscale='Viridis', opacity=0.8)
)
fig.add_trace(scatter)

fig.update_layout(
    scene=dict(
        xaxis=dict(title='X (cm)', range=[-100, 100], dtick=20),
        yaxis=dict(title='Y (cm)', range=[-100, 100], dtick=20),
        zaxis=dict(title='Z (cm)', range=[0, 100], dtick=20),
        bgcolor="black"
    ),
    scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.8)),
    title='3D 聲納掃描模擬（每秒刷新）'
)

display(fig)

# 模擬資料更新
for _ in range(5):
    new_x, new_y, new_z = [], [], []
    for theta in range(0, 180, 20):
        for phi in range(30, 90, 15):
            r = random.uniform(50, 100)
            theta_rad = math.radians(theta)
            phi_rad = math.radians(phi)
            x = r * math.sin(phi_rad) * math.cos(theta_rad)
            y = r * math.sin(phi_rad) * math.sin(theta_rad)
            z = r * math.cos(phi_rad)
            new_x.append(x)
            new_y.append(y)
            new_z.append(z)
    
    # 更新資料點
    with fig.batch_update():
        fig.data[0].x = new_x
        fig.data[0].y = new_y
        fig.data[0].z = new_z
        fig.data[0].marker.color = new_z

    time.sleep(1)
