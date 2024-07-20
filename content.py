import streamlit as st
import docx

from datetime import datetime

# Tạo một tiêu đề cho ứng dụng
st.title("Thời gian hiện tại")

# Lấy thời gian thực
current_time = datetime.now()

# Hiển thị thời gian hiện tại
st.write("Thời gian hiện tại:")
tm = current_time.strftime("%H:%M:%S")
st.write(current_time.strftime("%H:%M:%S"))
if (tm == '21:00:00'):

# print(type(t/m))
    # # Tạo một tiêu đề cho ứng dụng
    st.title("Các em truy cập vào link để tải bài xuống")
    def read_word_file(file_path):
        try:
            doc = docx.Document(file_path)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return content
        except FileNotFoundError:
            st.error("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
            return None
        except Exception as e:
            st.error(f"Đã xảy ra lỗi khi đọc file: {e}")
            return None

    # Đường dẫn tới file Word
    file_path = "id.docx"

    # Đọc và hiển thị nội dung file Word
    content = read_word_file(file_path)
    if content:
        st.write("Nội dung file Word:")
        st.write(content)
    else:
        st.write("Không thể hiển thị nội dung file Word.")
