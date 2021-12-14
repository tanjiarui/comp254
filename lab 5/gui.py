import hashlib, time
from tkinter import *

LOG_LINE_NUM = 0

class my_gui():
	def __init__(self,init_window_name):
		self.init_window_name = init_window_name

	def get_current_time(self):
		current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		return current_time

	# write log
	def write_log_to_Text(self, logmsg):
		global LOG_LINE_NUM
		current_time = self.get_current_time()
		logmsg_in = str(current_time) + ' ' + str(logmsg) + '\n'
		if LOG_LINE_NUM <= 7:
			self.log_data_Text.insert(END, logmsg_in)
			LOG_LINE_NUM = LOG_LINE_NUM + 1
		else:
			self.log_data_Text.delete(1.0, 2.0)
			self.log_data_Text.insert(END, logmsg_in)

	# function
	def str_trans_to_md5(self):
		src = self.init_data_Text.get(1.0, END).strip().replace('\n', '').encode()
		if src:
			try:
				myMd5 = hashlib.md5()
				myMd5.update(src)
				myMd5_Digest = myMd5.hexdigest()
				self.result_data_Text.delete(1.0, END)
				self.result_data_Text.insert(1.0, myMd5_Digest)
				self.write_log_to_Text('INFO: successful translation')
			except:
				self.result_data_Text.delete(1.0, END)
				self.result_data_Text.insert(1.0, 'fail to convert')
		else:
			self.write_log_to_Text('ERROR: fail to translate')

	# set window
	def set_init_window(self):
		self.init_window_name.title('text handler') # window name
		self.init_window_name.geometry('1068x681+10+10')
		# label
		self.init_data_label = Label(self.init_window_name, text='input')
		self.init_data_label.grid(row=0, column=0)
		self.result_data_label = Label(self.init_window_name, text='output')
		self.result_data_label.grid(row=0, column=10)
		self.log_label = Label(self.init_window_name, text='log')
		self.log_label.grid(row=10, column=0)
		# text
		self.init_data_Text = Text(self.init_window_name, width=60, height=30) # input
		self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
		self.result_data_Text = Text(self.init_window_name, width=60, height=30) # result
		self.result_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
		self.log_data_Text = Text(self.init_window_name, width=60, height=10) # log
		self.log_data_Text.grid(row=12, column=0, columnspan=10)
		# button
		self.str_trans_to_md5_button = Button(self.init_window_name, text='string to md5', bg='lightblue', width=10, command=self.str_trans_to_md5)
		self.str_trans_to_md5_button.grid(row=1, column=10)

init_window = Tk()
md5 = my_gui(init_window)
md5.set_init_window()
init_window.mainloop()