import Display_book
import Append_book
import Delete_book
import Search_book
import All_book
import Borrow_book
import Return_book
def operate(op_choice):
    # 用户选择操作界面，！登录后才可以选择
    if op_choice == '查看借书书单':
        Display_book.display_book()
    elif op_choice == '添加书籍':
        Append_book.append_book()
    elif op_choice == '删除书籍':
        Delete_book.delete_book()
    elif op_choice == '输入id查书':
        Search_book.search_book()
    elif op_choice == '查看书单':
        All_book.all_book()
    elif op_choice == '借书':
        Borrow_book.borrow_book()
    elif op_choice == '还书':
        Return_book.return_book()