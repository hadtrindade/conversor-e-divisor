from PySide2.QtCore import QThread, QObject, Signal, Slot


class SignalsToWorker(QObject):

    
    spinner =  Signal(object)
    pid_process = Signal(object)
    process_done = Signal(object)
    error = Signal(object)



class Worker(QThread):

    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = SignalsToWorker()

        self.kwargs['spinner_signal'] =  self.signal.spinner
        self.kwargs['done_signal'] = self.signal.process_done
        self.kwargs['pid_process_signal'] = self.signal.pid_process
        self.kwargs['error_signal'] = self.signal.error
        

    @Slot()
    def stop(self):
        self.terminate()
        
    @Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)