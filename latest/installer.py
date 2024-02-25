import os
os.system('cmd /c "pip install ttkbootstrap"')
os.system('cmd /c "pip install requests"')
import ttkbootstrap as ttk
from threading import Thread
import requests

class script():
    def juno():
        pass

    def download_and_install():
        action_count = 2
        accept_button.configure(command=script.juno, text='Installing...')
        url_l = 'https://thelecraft999.github.io/jarvis/latest/libs.txt'
        destination_l = f'{os.path.dirname(os.path.realpath(__file__))}/temp.txt'
        response = requests.get(url_l)
        if response.status_code == 200:
            with open(destination_l, 'wb') as file:
                file.write(response.content)
            with open(destination_l, 'r') as file:
                line_count = sum(1 for line in file)
        
        action_count = action_count + line_count

        progress_per_task = 100 / action_count

        try:
            with open(destination_l, 'r') as file:
                for line in file:
                    os.system(f'cmd /c "pip install {line.strip().lower()}"')
                    progressbar.step(progress_per_task)

        except FileNotFoundError:
            print(f"File not found: {destination_l}")
        except Exception as e:
            print(f"An error occurred: {e}")


        try:
            os.remove(destination_l)
            progressbar.step(progress_per_task)
        except FileNotFoundError:
            print(f"File not found: {destination_l}")
        except Exception as e:
            print(f"An error occurred: {e}")
        response = requests.get('https://thelecraft999.github.io/jarvis/latest/jarvis.py')
            
        if response.status_code == 200:
                with open(f'{os.path.dirname(os.path.realpath(__file__))}/jarvis.py', 'wb') as file:
                    file.write(response.content)
                    progressbar.step(progress_per_task - 0.0001)
                accept_button.configure(command=script.juno, text='Installed')
        else:
            print(f"Failed to download file. Status code: {response.status_code}")

    def check_checkboxes():
        if download_instructions.get() == 1:
            print('check')
            response = requests.get('https://thelecraft999.github.io/jarvis/latest/JARVIS_DOCUMENTATION.pdf')
            
            if response.status_code == 200:
                    with open(f'{os.path.dirname(os.path.realpath(__file__))}/documentation.pdf', 'wb') as file:
                        file.write(response.content)
            else:
                print(f"Failed to download file. Status code: {response.status_code}")

        if accept_tos.get() == 1:
            script.download_and_install()
        else:
            tos_label = ttk.Label(
                master=root,
                text='Please accept TOS, TOU, EULA'
            )
            tos_label.place(x=260,y=280)


    def execute_functions():
        t = Thread(target=script.check_checkboxes)
        t.start()    


if __name__ == '__main__':
    root = ttk.Window()
    root.title('JARVIS Installer -- 2.0')
    root.geometry('700x400')
    title_label = ttk.Label(master=root,
                                text='JARVIS Installer',
                                font='Calibri 24 bold')
    title_label.pack()
    progressbar = ttk.Progressbar()
    progressbar.place(x=100, y=100, width=500)    
        
    download_instructions = ttk.IntVar()
    accept_tos = ttk.IntVar()

    c1 = ttk.Checkbutton(root, text='Download Documentation-PDF', onvalue=1, offvalue=0, variable=download_instructions)
    c1.state(['!alternate'])
    c1.place(x=100, y=150)

    c2 = ttk.Checkbutton(root, text='I accept the TOS, TOU \nand EULA (https://thelecraft999.github.io/jarvis/tos)', onvalue=1, offvalue=0, variable=accept_tos)
    c2.state(['!alternate'])
    c2.place(x=100, y=175)
    
    accept_button = ttk.Button(master=root,
                                text='Download & Install',
                                command=script.execute_functions)
    accept_button.place(x=275, y=250)
    
    root.mainloop()