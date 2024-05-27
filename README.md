# Tom-and-Jerry-MazeGame
# Đồ án Game của nhóm 3 - lớp TNT1
## I.Hướng dẫn cài đặt 
- Đầu tiên , ta cần clone project về local bằng lệnh :
  ```
  git clone https://github.com/PhamNgocDuyPy/Tom-and-Jerry-MazeGame.git
  ```
- Cài đặt thư viện cần thiết pygame qua lệnh pip :
  ```
  python -m pip install pygame
  ```
- Chạy file 03.py và trải nghiệm
- Ngoài ra nhóm em còn làm một phần đăng nhập bằng Tkinter (trong folder login_ver2 )
## II Hướng dẫn chơi game :
- Người chơi sử dụng chuột để chọn trên menu và các phím mũi tên để di chuyển nhân vật , demo về các chức năng sẽ có tại video demo , mục tiêu là điều khiển Tâm bắt chú chuột Gia Huy quậy phá
- Có 3 chế độ chơi là **Easy mode , Normal mode và Hard mode** , người chơi có thể để game tự spawn vị trí của nhân vật Tâm và Gia Huy hoặc chỉ định vị trí của chúng bằng chuột
- Game sẽ tính toán số bước di chuyển phù hợp , nếu người chơi đi quá số bước sẽ thua , ngoài ra trên bản đồ còn có các viên phô mai cho nhân vật 1-5 bước
- Nếu cảm thấy không tìm được đường đi thì có thể nhấn nút **Hint** , game sẽ chỉ đường đi ngắn nhất để Tâm tiến tới bắt Gia Huy 
- Các nút thuật toán DFS BFS và BS sẽ tìm những đường đi tới với Gia Huy một cách nhanh nhất , lưu ý nếu dùng nó sẽ bị tính là thua cuộc
- Link demo youtube : [Youtube](https://youtu.be/SBz3HUezPuw)
