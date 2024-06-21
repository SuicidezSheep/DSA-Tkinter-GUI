#---Commputer Programming 2 Final PIT by: Liga
import ctypes
from tkinter import *
from tkinter import font
from tkinter import messagebox
from collections import deque

# #FF005C - pink-red
# #545151 - black-gray
# #FEF9CC - yellow
# Set the process DPI awareness
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def success_box():
        success_dialog = Tk()
        success_dialog.title('Successfully')
        success_dialog.resizable(width=False, height=False)
        success_dialog.geometry('300x80')
        success_dialog.config(bg='white') 
        success_txt = Label(success_dialog, text='Successfully, updated!', font=('Roboto', 10, 'italic', 'bold'), bg='white')
        success_txt.pack(pady=25)
        success_dialog.after(1000, success_dialog.destroy)

def RecursionFunction():
    
    def factorial_function(number):
        if number == 0:
            return 1
        else:
            return number * factorial_function(number - 1)
    
    def calculate_factorial():
        try:
            
            number = int(enter_number_entry.get())
            result = factorial_function(number)
            success_box()
            result_label.config(text=f'{result}', bg='white')
            enter_number_entry.delete(0, END)
            factorial_button.configure(bg='green')
            factorial_button.after(1000, reset_button)  # Delay for 1 second before resetting
        except ValueError:
            result_label.config(text='Please enter a valid number')
            factorial_button.configure(bg='red')
            factorial_button.after(1000, reset_button)  # Delay for 1 second before resetting

    def summing_function(number):
        if number == 0:
            return 1
        else:
            return number + summing_function(number - 1)
    
    def calculate_sum():
        try:
            number = int(enter_number_entry.get())
            result = summing_function(number)
            result_label.config(text=f'{result}', bg='white')
            enter_number_entry.delete(0, END)
            factorial_button.configure(bg='green')
            factorial_button.after(1000, reset_button)  # Delay for 1 second before resetting
        except ValueError:
            result_label.config(text='Please enter a valid number', fg='red')
            summing_button.configure(bg='red')
            summing_button.after(1000, reset_button)  # Delay for 1 second before resetting

    def reset_button():
        factorial_button.configure(bg='#545151')
        summing_button.configure(bg='#545151')

    recursion_window = Tk()
    recursion_window.geometry('500x500')
    recursion_window.title('Recursion')
    recursion_window.configure(bg='white')
    recursion_window.resizable(width=False, height=False)

    recursion_frame = Frame(recursion_window, width=300, height=360, bg='#FEF9CC')
    recursion_frame.place(x=100, y=80)
    txt = Label(recursion_frame, text='Choose Option', font=('Roboto', 12, 'bold'), bg='#FEF9CC')
    txt.place(x=80, y=10)
    greetings = Label(recursion_window, text='Recursion', font=('Roboto', 20, 'bold'), bg='white')
    greetings.pack(padx=0, pady=20)

    enter_number_entry = Entry(recursion_frame, width=30)
    enter_number_entry.place(x=25, y=55)
    enter_number_label = Label(recursion_frame, text='Enter number', font=('Roboto', 10), fg='black', bg='#FEF9CC')
    enter_number_label.place(x=95, y=80)

    factorial_button = Button(recursion_frame, width=20, text='Factorial', height=1, font=('Roboto', 12, 'bold'), bg='#545151', fg='white', command=calculate_factorial)
    factorial_button.place(x=20, y=110)

    summing_button = Button(recursion_frame, width=20, text='Summing', height=1, font=('Roboto', 12, 'bold'), bg='#545151', fg='white', command=calculate_sum)
    summing_button.place(x=20, y=160)

    result_frame = Frame(recursion_frame, width=250, height=70, bg='white')
    result_frame.place(x=20, y=215)
    result_label = Label(recursion_frame, text='Result', font=('Roboto', 10), bg='#FEF9CC')
    result_label.place(x=120, y=290)

    result_label = Label(result_frame, text=' ', font=('Roboto', 10, 'bold'), bg='white')
    result_label.place(x=20, y=25)

    def close_button():
        recursion_window.destroy()

    close_button = Button(recursion_frame, width=10, height=1, text='Close', bg='white', fg='red', font=('Roboto', 8, 'bold'), command=close_button)
    close_button.place(x=100, y=320)

def StackFunction():
    stack_elements = []
    def stack_action():
        nonlocal stack_elements

        try:
            input_text = stack_element_entry.get().strip()

            if input_text == '':
                update_button.config(bg='red')
                update_button.after(500, reset_button)
                stack_element_label.config(text=f'Empty entry!', font=('Roboto', 10, 'italic'), bg='white', fg='red')
            else:
                success_box() 
                push_button.config(state='active')
                pop_button.config(state='active')
                peek_button.config(state='active')
                clear_button.config(state='active')
                new_stack_element = input_text.split()
                stack_elements.extend(new_stack_element)
                update_button.config(bg='green')
                update_button.after(500, reset_button)
                stack_element_label.config(text=f'{stack_elements}', font=('Roboto', 10, 'bold'), bg='white')
                stack_element_entry.delete(0, END)
                    
        except ValueError:
            update_button.config(bg='red')
            update_button.after(500, reset_button)
            messagebox.showerror('Value error', 'Invalid input!')
            stack_element_label.config(text=f'Invalid input!', font=('Roboto', 10, 'bold', 'italic'), bg='white', )
        
    def clear_stack():
        clear_button.config(bg='green')
        clear_button.after(500, reset_button)
        stack_elements.clear()
        stack_element_label.config(text=f' ', bg='white')
        success_box()

    def reset_button():
        update_button.configure(bg='#545151')
        clear_button.configure(bg='#545151')
    def disable_button_funtion():
        push_button.config(state='disabled')
        pop_button.config(state='disabled')
        peek_button.config(state='disabled')

    def push_function():

        def push_element_func():
        
            new_push_element = new_push_entry.get()
            stack_elements.extend(new_push_element.split())
            success_box()
            push_window.destroy()
            updated_stack_label.config(text=stack_elements, font=('Roboto', 10, 'italic'))

        push_window = Tk()
        push_window.geometry('400x300')
        push_window.resizable(width=False, height=False)
        push_window.title('Stack: Pop')
        push_window.config(bg='white')
        label_stack = Label(push_window, text='Push Element', font=('Roboto', 15, 'bold'), bg='white')
        label_stack.place(x=120, y=10)
        newframe_current_stack = Frame(push_window, width=300, height=200, bg='#FEF9CC')
        newframe_current_stack.place(x=50, y=50)
        newframe_current_stack2 = Frame(newframe_current_stack, width=250, height=30, bg='white')
        newframe_current_stack2.place(x=20, y=25)
        current_stack_label = Label(newframe_current_stack, text=f'{stack_elements}', font=('Roboto', 10, 'italic'), bg='white')
        current_stack_label.place(x=20, y=27)
        txt3 = Label(newframe_current_stack, text='current stack', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        txt3.place(x=100, y=60)

        new_push_entry = Entry(newframe_current_stack, width=31, bg='white')
        new_push_entry.place(x=20, y=90)
        push_txt = Label(newframe_current_stack, text='Enter new element to push', font=('Roboto', 10, 'bold'), bg='#FEF9CC')
        push_txt.place(x=40, y=122)

        push_element_button = Button(newframe_current_stack, text='Update stack', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=push_element_func)
        push_element_button.place(x=80, y=155)

    def pop_function():
        pop_window = Tk()
        pop_window.geometry('300x80')
        pop_window.resizable(width=False, height=False)
        pop_window.config(bg='white')

        if stack_elements:
            pop_window.title('Pop element')
            popped_element = stack_elements.pop()
            success_txt = Label(pop_window, text=f'Pop element is: {popped_element}', font=('Roboto', 10, 'italic', 'bold'), bg='white')
            updated_stack_label.config(text=stack_elements, font=('Roboto', 10, 'italic'))
            

        else:
            pop_window.title('Empty stack')
            success_txt = Label(pop_window, text='Empty list stack!', font=('Roboto', 10, 'italic', 'bold'), bg='white')
            updated_stack_label.config(text=stack_elements, font=('Roboto', 10, 'italic'))

        success_txt.place(x=80, y=25)
        pop_window.after(1000, pop_window.destroy)

    def peek_function():
        peek_window = Tk()
        peek_window.geometry('400x150')
        peek_window.resizable(width=True, height=False)
        peek_window.config(bg='white')

        peek_window.title('Peek element')
        peek_txt = Label(peek_window, text=f'Current stack', font=('Roboto', 15, 'italic', 'bold'), bg='white')
        peek_txt.pack(padx=10, pady=10)
        
        success_txt = Label(peek_window, text=f'{stack_elements}', font=('Roboto', 10, 'italic', 'bold'), bg='white')
        updated_stack_label.config(text=stack_elements, font=('Roboto', 10, 'italic'))
        success_txt.place(x=80, y=60)

        def peek_close():
            peek_window.destroy()

        peek_close_button = Button(peek_window, text='Close', width=10, height=1, font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=peek_close)
        peek_close_button.place(x=150, y=100)

    stack_window = Tk()
    stack_window.geometry('600x700')
    stack_window.title('Stack')
    stack_window.configure(bg='white')
    stack_window.resizable(width=False, height=False)

    stack_frame = Frame(stack_window, width=400, height=250, bg='#FEF9CC')
    stack_frame.place(x=100, y=80)
    txt = Label(stack_frame, text='Enter element of the stack', font=('Roboto', 12, 'bold'), bg='#FEF9CC')
    txt.place(x=70, y=20)
    txt2 = Label(stack_frame, text='(separated with spaces)', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
    txt2.place(x=135, y= 90)
    greetings = Label(stack_window, text='Stack', font=('Roboto', 20, 'bold'), bg='white')
    greetings.pack(padx=0, pady=20)

    stack_element_entry = Entry(stack_frame, width=35)
    stack_element_entry.place(x=60, y=60)

    update_button = Button(stack_frame, text='Update Stack', command=stack_action, font=('Roboto', 10, 'bold'), bg='#545151', fg='white')
    update_button.place(x=80, y=120)

    clear_button = Button(stack_frame, text='Clear Stack', command=clear_stack, font=('Roboto', 10, 'bold'), bg='#545151', fg='white')
    clear_button.place(x=220, y=120)

    stack_result_frame = Frame(stack_frame, width=280, height=40, bg='white')
    stack_result_frame.place(x=60, y=170)

    stack_element_label = Label(stack_result_frame, text=' ', bg='white')
    stack_element_label.place(x=20, y=8)
    txt3 = Label(stack_frame, text='current stack', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
    txt3.place(x=160, y=215)

    stack_frame2 = Frame(stack_window, width=400, height=280, bg='#FEF9CC')
    stack_frame2.place(x=100, y=350)

    option_txt = Label(stack_frame2, text='Choose Option', font=('Roboto', 12, 'bold'), bg='#FEF9CC')
    option_txt.place(x=120, y=20)

    push_button = Button(stack_frame2, width=8, height=1, text='Push', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=push_function,state='disabled')
    push_button.place(x=50, y=170)
    pop_button = Button(stack_frame2, width=8, height=1, text='Pop', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=pop_function, state='disabled')
    pop_button.place(x=150, y=170)
    peek_button = Button(stack_frame2, width=8, height=1, text='Peek', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=peek_function, state='disabled')
    peek_button.place(x=250, y=170)
    
    stack_result_frame2 = Frame(stack_frame2, width=290, height=60, bg='white')
    stack_result_frame2.place(x=50, y=60)

    updated_stack_txt = Label(stack_frame2, text='Updated stack', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
    updated_stack_txt.place(x=150, y=130)
    updated_stack_label = Label(stack_result_frame2, text=stack_elements, font=('Roboto', 10, 'bold'), bg='white')
    updated_stack_label.place(x=10, y=20)

    def stack_frame_clear():
        updated_stack_label.config(text='')
        success_box()

    def close_button():
        stack_window.destroy()

    close_button = Button(stack_frame2, width=8, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_button)
    close_button.place(x=150, y=220)

    clear_button = Button(stack_frame2, text='Clear', width=8, height=1, font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=stack_frame_clear, state='disabled')
    clear_button.place(x=250, y=220)

    disable_button = Button(stack_frame2, text='Disable', width=8, height=1, font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=disable_button_funtion)
    disable_button.place(x=50, y=220)

def QueueFunction():

    Queue_list = []

    def enqueue_func():
        
        def enqueue_action():
            nonlocal Queue_list

            element_list = queue_element_entry.get().split()
            Queue_list.extend(element_list)

            new_enqueue_elements = enqueue_entry.get().strip().split()
            Queue_list.append(new_enqueue_elements)

            queue_result_label.config(text=f'Result: {Queue_list}')
            success_box()
            enqueue_window.destroy()
            queue_element_entry.delete(0, END)

        enqueue_window = Tk()
        enqueue_window.geometry('500x300')
        enqueue_window.title('Enqueue')
        enqueue_window.configure(bg='white')
        enqueue_window.resizable(width=False, height=False)
        greetings2 = Label(enqueue_window, text='Enqueue', font=('Roboto', 20, 'bold'), bg='white')
        greetings2.pack(padx=0, pady=20)
        enqueue_frame = Frame(enqueue_window, width=400, height=150, bg='#FEF9CC')
        enqueue_frame.place(x=50, y=70)

        enqueue_entry = Entry(enqueue_frame, width=30, bg='white')
        enqueue_entry.place(x=80, y=30)
        txt_que = Label(enqueue_frame, text='Enter the element to enqueue', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        txt_que.place(x=110, y= 60)
        enqueue_button = Button(enqueue_frame, width=15, height=1, text='Update Queue', font=('Roboto', 10, 'bold'), fg='white', bg='#545151', command=enqueue_action)
        enqueue_button.place(x=120, y=100)
    
    def reverse_func():

        def reverse_action():
            nonlocal Queue_list
            
            queue_result_label.config(text=f'Result: {Queue_list}')
            reverse_window.destroy()
            queue_element_entry.delete(0, END)
            success_box()

        reverse_window = Tk()
        reverse_window.geometry('500x350')
        reverse_window.title('Reverse Queue')
        reverse_window.configure(bg='white')
        reverse_window.resizable(width=False, height=False)
        greetings3 = Label(reverse_window, text='Reverse Queue', font=('Roboto', 20, 'bold'), bg='white')
        greetings3.pack(padx=0, pady=20)
        reverse_frame = Frame(reverse_window, width=400, height=250, bg='#FEF9CC')
        reverse_frame.place(x=50, y=70)

        reverse_frame2 = Frame(reverse_frame, width=350, height=40, bg='white')
        reverse_frame2.place(x=25, y=20)

        element_lists = queue_element_entry.get().strip().split()
        Queue_list.extend(element_lists)

        current_queue_label = Label(reverse_frame2, text=f'Result: {Queue_list}', font=('Roboto', 10, 'bold'),  bg='white')
        current_queue_label.place(x=10, y=10)
        current_label_txt = Label(reverse_frame, text='Current queue', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        current_label_txt.place(x=150, y=60)

        reverse_frame3 = Frame(reverse_frame, width=350, height=40, bg='white')
        reverse_frame3.place(x=25, y=120)

        Queue_list.reverse()

        reverse_queue_label = Label(reverse_frame3, text=f'Result: {Queue_list} ', font=('Roboto', 10, 'bold'),  bg='white')
        reverse_queue_label.place(x=10, y=10)
           
        reverse_button = Button(reverse_frame, width=15, height=1, text='Reverse Queue', font=('Roboto', 10, 'bold'), fg='white', bg='#545151', command=reverse_action)
        reverse_button.place(x=120, y=200)
        reverse_label_txt = Label(reverse_frame, text='Reverse queue', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        reverse_label_txt.place(x=150, y=160)
    
    def add_queue_func():

        def add_queue_action():
            nonlocal Queue_list

            queued_entry = queue_element_entry.get().split()
            Queue_list.extend(queued_entry)

            added_queue_element = add_element_entry.get().strip()
            Queue_list.append(added_queue_element)
            queue_result_label.config(text=f'Result: {Queue_list}')
            add_queue_window.destroy()
            queue_element_entry.delete(0, END)
            success_box()

        add_queue_window = Tk()
        add_queue_window.geometry('500x350')
        add_queue_window.title('Add Element Queue')
        add_queue_window.configure(bg='white')
        add_queue_window.resizable(width=False, height=False)
        greetings4 = Label(add_queue_window, text='Add Element Queue', font=('Roboto', 20, 'bold'), bg='white')
        greetings4.pack(padx=0, pady=20)
        add_queue_frame = Frame(add_queue_window, width=400, height=250, bg='#FEF9CC')
        add_queue_frame.place(x=50, y=70)

        add_queue_frame2 = Frame(add_queue_frame, width=350, height=40, bg='white')
        add_queue_frame2.place(x=25, y=20)

        current_queue_label = Label(add_queue_frame2, text=f'Result: {Queue_list}', font=('Roboto', 10, 'bold'),  bg='white')
        current_queue_label.place(x=10, y=10)

        current_label_txt = Label(add_queue_frame, text='Current queue', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        current_label_txt.place(x=160, y=60)

        add_element_entry = Entry(add_queue_frame, width=43)
        add_element_entry.place(x=25, y=120)
        add_label_txt = Label(add_queue_frame, text='Add element queue', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
        add_label_txt.place(x=150, y=150)

        add_element_button = Button(add_queue_frame, width=15, height=1, text='Add element', font=('Roboto', 10, 'bold'), fg='white', bg='#545151', command=add_queue_action)
        add_element_button.place(x=120, y=200)

    def dequeue_func():
        nonlocal Queue_list

        element_list = queue_element_entry.get().strip().split()
        Queue_list.extend(element_list)
        queue_element_entry.delete(0, END)

        if Queue_list:
            pop_element = Queue_list[0]
            Queue_list.pop(0)
            queue_result_label.config(text=f'Result: Pop: {pop_element} || {Queue_list}')
            success_box()
        else:
            queue_result_label.config(text=f'Result: Empty queue list!')
            

    def queue_label_clear():
        queue_result_label.config(text=f' ', bg='white')
        Queue_list.clear()
        success_box()

    def close_queue():
        queued_window.destroy()

    queued_window = Tk()
    queued_window.geometry('500x550')
    queued_window.title('Queue')
    queued_window.configure(bg='white')
    queued_window.resizable(width=False, height=False)

    queued_frame = Frame(queued_window, width=400, height=350, bg='#FEF9CC')
    queued_frame.place(x=50, y=80)
    txt = Label(queued_frame, text='Enter element of the queue', font=('Roboto', 12, 'bold'), bg='#FEF9CC')
    txt.place(x=70, y=20)
    txt2 = Label(queued_frame, text='(separated with spaces)', font=('Roboto', 8, 'italic'), bg='#FEF9CC')
    txt2.place(x=135, y= 90)
    greetings = Label(queued_window, text='Queue', font=('Roboto', 20, 'bold'), bg='white')
    greetings.pack(padx=0, pady=20)

    queue_element_entry = Entry(queued_frame, width=35)
    queue_element_entry.place(x=60, y=60)

    enqueue_button = Button(queued_frame, width=13, height=1, text='Enqueue', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=enqueue_func)
    enqueue_button.place(x=60, y=120)

    reverse_button = Button(queued_frame, width=13, height=1, text='Reverse', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=reverse_func)
    reverse_button.place(x=205, y=120)
    
    add_button = Button(queued_frame, width=13, height=1, text='Add Queue', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=add_queue_func)
    add_button.place(x=60, y=160)

    dequeued_button = Button(queued_frame, width=13, height=1, text='Dequeued', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=dequeue_func)
    dequeued_button.place(x=205, y=160)

    queue_result_frame = Frame(queued_frame, width=290, height=60, bg='white')
    queue_result_frame.place(x=55, y=220)

    queue_result_label = Label(queue_result_frame, text='Result: ', font=('Roboto', 10, 'bold'), bg='white')
    queue_result_label.place(x=10, y=20)

    clear_queue_button = Button(queued_frame, width=13, height=1, text='Clear', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=queue_label_clear)
    clear_queue_button.place(x=130, y=300)

    queued_close_button = Button(queued_window, width=13, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_queue)
    queued_close_button.place(x=180, y=470)

def SortingAlgoFunction():
    def bubble_sort_func():
        def bubble_action():
            element_list = element_list_entry.get().strip().split()
            Element_list = list(map(int, element_list))
            success_box()

            n = len(Element_list)
            passes = []
            for i in range(n):
                for j in range(0, n-i-1):
                    if Element_list[j] > Element_list[j+1]:
                        Element_list[j], Element_list[j+1] = Element_list[j+1], Element_list[j]
                passes.append(f'Pass {i + 1}: {Element_list.copy()}')
                update_pass_display(passes)

            sorted_result_label.config(text=f'Sorted: {Element_list}')

        def update_pass_display(passes):
            passes_label.config(text="\n".join(passes))
            bubble_window.update_idletasks()

        bubble_window = Tk()
        bubble_window.title('Bubble-sort Algorithm')
        bubble_window.geometry('700x600')
        bubble_window.resizable(width=False, height=False)
        bubble_window.config(bg='white')

        greetings = Label(bubble_window, text='Bubble Sort Algorithm', font=('Roboto', 20, 'bold'), bg='white')
        greetings.pack(padx=0, pady=20)
        
        bubble_frame = Frame(bubble_window, width=600, height=480, bg='#FEF9CC')
        bubble_frame.place(x=50, y=100)

        element_list_entry = Entry(bubble_frame, width=40, bg='white')
        element_list_entry.place(x=140, y=50)
        element_list_txt = Label(bubble_frame, text="Enter numbers (Separated by spaces)", font=('Roboto', 10, 'italic'), bg='#FEF9CC')
        element_list_txt.place(x=155, y=80)

        sort_button = Button(bubble_frame, width=13, height=1, text='Sort', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=bubble_action)
        sort_button.place(x=230, y=130)

        sorted_frame_result = Frame(bubble_frame, width=490, height=200, bg='white')
        sorted_frame_result.place(x=55, y=200)

        passes_label =Label(sorted_frame_result, text='', font=('Roboto', 10, 'italic'), bg='white', justify='left')
        passes_label.place(x=20, y=10)

        def close_bubble_window():
            bubble_window.destroy()

        close_button = Button(bubble_frame, width=13, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_bubble_window)
        close_button.place(x=230, y=430)

    def selection_sort_func():
        def selection_action():
            success_box()
            element_list = element_list_entry.get().strip().split()
            Element_list = list(map(int, element_list))

            n = len(Element_list)
            passes = []
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    if Element_list[j] < Element_list[min_idx]:
                        min_idx = j
                Element_list[i], Element_list[min_idx] = Element_list[min_idx], Element_list[i]
                passes.append(f'Pass {i + 1}: {Element_list.copy()}')
                update_pass_display(passes)

            sorted_result_label.config(text=f'Sorted: {Element_list}')

        def update_pass_display(passes):
            passes_label.config(text="\n".join(passes))
            selection_window.update_idletasks()


        selection_window = Tk()
        selection_window.title('Selection-sort Algorithm')
        selection_window.geometry('700x600')
        selection_window.resizable(width=False, height=False)
        selection_window.config(bg='white')

        greetings = Label(selection_window, text='Selection Sort Algorithm', font=('Roboto', 20, 'bold'), bg='white')
        greetings.pack(padx=0, pady=20)
        
        selection_frame = Frame(selection_window, width=600, height=480, bg='#FEF9CC')
        selection_frame.place(x=50, y=100)

        element_list_entry = Entry(selection_frame, width=40, bg='white')
        element_list_entry.place(x=140, y=50)
        element_list_txt = Label(selection_frame, text="Enter numbers (Separated by spaces)", font=('Roboto', 10, 'italic'), bg='#FEF9CC')
        element_list_txt.place(x=155, y=80)

        sort_button = Button(selection_frame, width=13, height=1, text='Sort', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=selection_action)
        sort_button.place(x=230, y=130)

        sorted_frame_result = Frame(selection_frame, width=490, height=200, bg='white')
        sorted_frame_result.place(x=55, y=200)

        passes_label =Label(sorted_frame_result, text='', font=('Roboto', 10, 'italic'), bg='white')
        passes_label.place(x=20, y=10)

        def close_selection_window():
            selection_window.destroy()
            
        close_button = Button(selection_frame, width=13, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_selection_window)
        close_button.place(x=230, y=430)
        
    def insertion_sort_func():
        def insertion_action():
            success_box()
            element_list = element_list_entry.get().strip().split()
            Element_list = list(map(int, element_list))

            passes = []
            for i in range(1, len(Element_list)):
                key = Element_list[i]
                j = i-1
                while j >= 0 and key < Element_list[j]:
                    Element_list[j + 1] = Element_list[j]
                    j -= 1
                Element_list[j + 1] = key
                passes.append(f'Pass {i}: {Element_list.copy()}')
                update_pass_display(passes)

            sorted_result_label.config(text=f'Sorted: {Element_list}')

        def update_pass_display(passes):
            passes_label.config(text="\n".join(passes))
            insertion_window.update_idletasks()

        insertion_window = Tk()
        insertion_window.title('Insertion-sort Algorithm')
        insertion_window.geometry('700x600')
        insertion_window.resizable(width=False, height=False)
        insertion_window.config(bg='white')

        greetings = Label(insertion_window, text='Insertion Sort Algorithm', font=('Roboto', 20, 'bold'), bg='white')
        greetings.pack(padx=0, pady=20)
        
        insertion_frame = Frame(insertion_window, width=600, height=480, bg='#FEF9CC')
        insertion_frame.place(x=50, y=100)

        element_list_entry = Entry(insertion_frame, width=40, bg='white')
        element_list_entry.place(x=140, y=50)
        element_list_txt = Label(insertion_frame, text="Enter numbers (Separated by spaces)", font=('Roboto', 10, 'italic'), bg='#FEF9CC')
        element_list_txt.place(x=155, y=80)

        sort_button = Button(insertion_frame, width=13, height=1, text='Sort', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=insertion_action)
        sort_button.place(x=230, y=130)

        sorted_frame_result = Frame(insertion_frame, width=490, height=200, bg='white')
        sorted_frame_result.place(x=55, y=200)

        passes_label =Label(sorted_frame_result, text='', font=('Roboto', 10, 'italic'), bg='white')
        passes_label.place(x=20, y=10)

        def close_insertion_window():
            insertion_window.destroy()
            
        close_button = Button(insertion_frame, width=13, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_insertion_window)
        close_button.place(x=230, y=430)

    sorting_window = Tk()
    sorting_window.geometry('700x530')
    sorting_window.title('Sorting Algorithms')
    sorting_window.configure(bg='white')
    sorting_window.resizable(width=False, height=False)
    greetings = Label(sorting_window, text='Sorting Algorithms', font=('Roboto', 20, 'bold'), bg='white')
    greetings.pack(padx=0, pady=20)

    sorting_frame = Frame(sorting_window, width=580, height=400, bg='#FEF9CC')
    sorting_frame.place(x=60, y=80)
    txt = Label(sorting_frame, text='Choose Option', font=('Roboto', 15, 'bold'), bg='#FEF9CC')
    txt.place(x=220, y=20)

    bubble_sort_button = Button(sorting_frame, width=17, height=1, text='Bubble Sorting', font=('Roboto', 11, 'bold'), bg='#545151', fg='white', command=bubble_sort_func)
    bubble_sort_button.place(x=200, y=80)

    selection_sort_button = Button(sorting_frame, width=17, height=1, text='Selection Sorting', font=('Roboto', 11, 'bold'), bg='#545151', fg='white', command=selection_sort_func)
    selection_sort_button.place(x=200, y=130)

    insertion_sort_button = Button(sorting_frame, width=17, height=1, text='Insertion Sorting', font=('Roboto', 11, 'bold'), bg='#545151', fg='white', command=insertion_sort_func)
    insertion_sort_button.place(x=200, y=180)


    sorted_result_frame = Frame(sorting_frame, width=460, height=70, bg='white')
    sorted_result_frame.place(x=60, y=250)

    sorted_result_label = Label(sorted_result_frame, text=f'Sorted: ', font=('Roboto', 10, 'bold'), bg='white')
    sorted_result_label.place(x=20, y=25)
    

    def close_button():
        sorting_window.destroy()

    sorting_window_close_button = Button(sorting_window, width=13, height=1, text='Close', font=('Roboto', 10, 'bold'), bg='#545151', fg='white', command=close_button)
    sorting_window_close_button.place(x=280, y=430)

root = Tk()
root.title('Comprog PIT Finals')
root.geometry('1000x1000')
root.resizable(width=False, height=False)
root.configure(bg='white')
default_bg = '#FF005C'
default_font_color = 'white'

header_frame = Frame(root, width=1000, height=80, bg=default_bg)
header_frame.place(x=0, y=0)

header_text = Label(header_frame, text='Computer Programming 2 Final P.I.T', font=('Roboto', 20, 'bold'), bg=default_bg, fg=default_font_color)
header_text.place(x=240, y=22)

canvas_frame = Frame(root, width=653, height=596, bg='#FEF9CC')
canvas_frame.place(x=174, y=217)

canvas_frame_header = Frame(canvas_frame, width=653, height=100, bg='#545151')
canvas_frame_header.place(x=0, y=0)
canvas_frame_header_text = Label(canvas_frame_header, text='Choose Action', font=('Roboto', 15, 'bold'), fg=default_font_color, bg='#545151')
canvas_frame_header_text.place(x=250, y=35)

recursion_button = Button(canvas_frame, text='Recursion', width=30, height=2, font=('Roboto', 15, 'bold'), fg=default_font_color, bg='#545151', command=RecursionFunction)
recursion_button.place(x=100, y=150)

stack_button = Button(canvas_frame, text='Stack', width=30, height=2, font=('Roboto', 15, 'bold'), fg=default_font_color, bg='#545151', command=StackFunction)
stack_button.place(x=100, y=250)

queue_button = Button(canvas_frame, text='Queue', width=30, height=2, font=('Roboto', 15, 'bold'), fg=default_font_color, bg='#545151', command=QueueFunction)
queue_button.place(x=100, y=350)

sorting_algo_button = Button(canvas_frame, text='Sorting Algorithm', width=30, height=2, font=('Roboto', 15, 'bold'), fg=default_font_color, bg='#545151', command=SortingAlgoFunction)
sorting_algo_button.place(x=100, y=450)

owner_label = Label(root, text='by: Liga, Alther Adrian P. IT1R7', font=('Roboto', 7, 'italic'), bg='white')
owner_label.place(x=10, y=960)

root.mainloop()

# --by: Liga, Alther Adrian P.
#---GitHub: SuicidezSheep
#---Gmail: altheradrian@gmail.com