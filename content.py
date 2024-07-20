import streamlit as st
import docx

# Tạo một tiêu đề cho ứng dụng
st.title("Các em truy cập vào link để tải bài xuống")

# Đọc nội dung file Word
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
