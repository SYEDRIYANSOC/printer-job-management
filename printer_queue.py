class PrinterQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, document_name):
        self.queue.append(document_name)
        print(f"Added to print queue: '{document_name}'")

    def print_next_job(self):
        if len(self.queue) > 0:
            printed_doc = self.queue.pop(0)
            print(f"Printing... -> '{printed_doc}' completed.")
        else:
            print("No print jobs in the queue. Printer is idle.")

    def show_queue(self):
        if self.queue:
            print(f"Current Print Queue: {self.queue}")
        else:
            print("The print queue is currently empty.")

# --- Testing the Implementation ---
printer = PrinterQueue()
printer.add_job("Math_Assignment.pdf")
printer.add_job("Resume.docx")
printer.add_job("Ticket.pdf")
printer.show_queue()
printer.print_next_job()
printer.print_next_job()
printer.show_queue()