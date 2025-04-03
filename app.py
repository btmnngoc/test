pip install dash dash-bootstrap-components plotly pandas
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Khởi tạo ứng dụng Dash với Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dữ liệu giả lập (thay thế bằng dữ liệu thực của bạn)
# Dữ liệu tổng quan
summary_data = {
    "Tổng doanh thu": "1,034 Tỷ VNĐ",
    "Tổng lợi nhuận": "344,71 Tỷ VNĐ",
    "Giá trị mỗi đơn hàng": "105,42 Tr VNĐ",
    "Biến lợi nhuận": "33,33%"
}

# Dữ liệu doanh thu, lợi nhuận theo tháng
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
doanh_thu = [50, 60, 70, 80, 90, 100, 80, 70, 60, 50, 40, 30]
loi_nhuan = [10, 15, 20, 25, 30, 35, 25, 20, 15, 10, 5, 0]

df_doanh_thu = pd.DataFrame({
    "Tháng": months,
    "Doanh thu": doanh_thu,
    "Lợi nhuận": loi_nhuan
})

# Dữ liệu phân loại đơn hàng
df_don_hang = pd.DataFrame({
    "Loại": ["Phi doanh thu", "Chi nhánh Đà Nẵng", "Chi nhánh Hà Nội", "Chi nhánh Hồ Chí Minh"],
    "Giá trị": [10000, 344714, 200000, 150000]
})

# Dữ liệu KPI theo tháng
kpi_data = pd.DataFrame({
    "Tháng": months,
    "Doanh thu": [50, 60, 70, 80, 90, 100, 80, 70, 60, 50, 40, 30],
    "Lợi nhuận": [10, 15, 20, 25, 30, 35, 25, 20, 15, 10, 5, 0],
    "Tạo doanh thu": [5, 10, 15, 20, 25, 30, 20, 15, 10, 5, 0, 0]
})

# Dữ liệu tăng trưởng doanh thu theo chi nhánh
df_tang_truong = pd.DataFrame({
    "Tháng": list(range(1, 13)) * 3,
    "Doanh thu": [20, 25, 30, 35, 40, 45, 40, 35, 30, 25, 20, 15] +  # Chi nhánh Đà Nẵng
                 [30, 35, 40, 45, 50, 55, 50, 45, 40, 35, 30, 25] +  # Chi nhánh Hà Nội
                 [40, 45, 50, 55, 60, 65, 60, 55, 50, 45, 40, 35],   # Chi nhánh Hồ Chí Minh
    "Chi nhánh": ["Chi nhánh Đà Nẵng"] * 12 + ["Chi nhánh Hà Nội"] * 12 + ["Chi nhánh Hồ Chí Minh"] * 12
})

# Tạo các biểu đồ
# Biểu đồ cột: Doanh thu, lợi nhuận theo tháng
fig_doanh_thu = go.Figure()
fig_doanh_thu.add_trace(go.Bar(x=df_doanh_thu["Tháng"], y=df_doanh_thu["Doanh thu"], name="Doanh thu", marker_color="blue"))
fig_doanh_thu.add_trace(go.Bar(x=df_doanh_thu["Tháng"], y=df_doanh_thu["Lợi nhuận"], name="Lợi nhuận", marker_color="orange"))
fig_doanh_thu.update_layout(title="Doanh thu, lợi nhuận theo tháng", barmode="group")

# Biểu đồ tròn: Phân loại đơn hàng
fig_don_hang = px.pie(df_don_hang, values="Giá trị", names="Loại", title="Phân loại đơn hàng")

# Biểu đồ KPI theo tháng
fig_kpi = go.Figure()
fig_kpi.add_trace(go.Bar(x=kpi_data["Tháng"], y=kpi_data["Doanh thu"], name="Doanh thu", marker_color="blue"))
fig_kpi.add_trace(go.Bar(x=kpi_data["Tháng"], y=kpi_data["Lợi nhuận"], name="Lợi nhuận", marker_color="orange"))
fig_kpi.add_trace(go.Scatter(x=kpi_data["Tháng"], y=kpi_data["Tạo doanh thu"], name="Tạo doanh thu", mode="lines+markers", marker_color="green"))
fig_kpi.update_layout(title="Đánh giá KPI")

# Biểu đồ đường: Tăng trưởng doanh thu theo chi nhánh
fig_tang_truong = px.line(df_tang_truong, x="Tháng", y="Doanh thu", color="Chi nhánh", title="Tăng trưởng doanh thu")

# Layout của dashboard
app.layout = dbc.Container([
    # Tiêu đề
    html.H1("TỔNG QUAN", className="text-center mt-4 mb-4", style={"color": "black"}),

    # Số liệu tổng quan
    dbc.Row([
        dbc.Col(dbc.Card([
            html.H5("Tổng doanh thu", className="card-title text-center"),
            html.P(summary_data["Tổng doanh thu"], className="card-text text-center", style={"fontSize": "24px", "color": "black"})
        ], body=True, className="shadow-sm"), md=3),
        dbc.Col(dbc.Card([
            html.H5("Tổng lợi nhuận", className="card-title text-center"),
            html.P(summary_data["Tổng lợi nhuận"], className="card-text text-center", style={"fontSize": "24px", "color": "black"})
        ], body=True, className="shadow-sm"), md=3),
        dbc.Col(dbc.Card([
            html.H5("Giá trị mỗi đơn hàng", className="card-title text-center"),
            html.P(summary_data["Giá trị mỗi đơn hàng"], className="card-text text-center", style={"fontSize": "24px", "color": "black"})
        ], body=True, className="shadow-sm"), md=3),
        dbc.Col(dbc.Card([
            html.H5("Biến lợi nhuận", className="card-title text-center"),
            html.P(summary_data["Biến lợi nhuận"], className="card-text text-center", style={"fontSize": "24px", "color": "black"})
        ], body=True, className="shadow-sm"), md=3),
    ], className="mb-4"),

    # Biểu đồ
    dbc.Row([
        # Biểu đồ cột
        dbc.Col(dcc.Graph(figure=fig_doanh_thu), md=6),
        # Biểu đồ tròn
        dbc.Col(dcc.Graph(figure=fig_don_hang), md=6),
    ], className="mb-4"),

    dbc.Row([
        # Biểu đồ KPI
        dbc.Col(dcc.Graph(figure=fig_kpi), md=6),
        # Biểu đồ đường
        dbc.Col(dcc.Graph(figure=fig_tang_truong), md=6),
    ])
], fluid=True)

# Chạy ứng dụng
if __name__ == "__main__":
    app.run_server(debug=True)
