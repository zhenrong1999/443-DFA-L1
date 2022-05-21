import tkinter as tk

from tkinter import filedialog as fd
from tkinter import ttk

import src.DFA as DFA
import src.source as fileManagement


class UI:
    seperatorChar = [" ", ",", ".", "\n"]

    def __init__(self, root):
        dictionaryList = fileManagement.readFile("data\ListOfPlace.txt")
        self.t = DFA.Dfa()
        self.patternFound = {}
        for key in dictionaryList:
            self.t.initializeDfaState(key)
        root.title("DFA Simple Machine")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        # Input Text
        sampleTextFrame = ttk.Frame(mainframe, padding="3 3 12 12")
        sampleTextFrame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        sampleTextLabel = ttk.Label(sampleTextFrame, text="Input Text")
        sampleTextLabel.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.sampleText = tk.Text(sampleTextFrame)
        self.sampleText.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.W, tk.E))

        # Output Text
        resultTextFrame = ttk.Frame(mainframe, padding="3 3 12 12")
        resultTextFrame.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.W, tk.E))
        resultTextLabel = ttk.Label(resultTextFrame, text="Output Text")
        resultTextLabel.grid(column=0, row=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.resultText = tk.Text(resultTextFrame)
        self.resultText.grid(column=0, row=3, sticky=(tk.N, tk.S, tk.W, tk.E))
        # file button
        buttonFrame = ttk.Frame(mainframe, padding="3 3 12 12")
        buttonFrame.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.fileButton = ttk.Button(
            buttonFrame, text="Open txt File", command=self.fileButtonClicked
        )
        self.fileButton.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.dictionaryButton = ttk.Button(
            buttonFrame, text="Choose dictionary", command=self.dictionaryButtonClicked
        )
        self.dictionaryButton.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        infoTextFrame = ttk.Frame(mainframe, padding="3 3 12 12")
        infoTextFrame.grid(column=1, row=1, sticky=(tk.N, tk.S, tk.W, tk.E))
        infoTextFrame.columnconfigure(0, weight=3)
        infoTextFrame.rowconfigure(0, weight=3)
        infoTextLabel = ttk.Label(infoTextFrame, text="Info")
        infoTextLabel.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.infoText = tk.Text(infoTextFrame)
        self.infoText.grid(column=0, row=1, sticky=(tk.S, tk.E))

    def executeOnText(self, func):
        self.sampleText.config(state="normal")
        self.resultText.config(state="normal")
        func()
        self.sampleText.config(state="disabled")
        self.resultText.config(state="disabled")

    def executeOnInfoText(self, func):
        self.infoText.config(state="normal")
        func()
        self.infoText.config(state="disabled")

    def dictionaryButtonClicked(self):
        filetypes = (("text files", "*.txt"), ("All files", "*.*"))
        filename = fd.askopenfilename(
            title="Open a file", initialdir="./", filetypes=filetypes
        )
        dictionaryList = fileManagement.readFile(filename)
        self.t = DFA.Dfa()
        for key in dictionaryList:
            self.t.initializeDfaState(key)
        # Prompt user for success
        self.executeOnInfoText(lambda: self.infoText.delete(1.0, tk.END))
        self.executeOnInfoText(
            lambda: self.infoText.insert(tk.END, "Dictionary loaded")
        )
        # Check if result is empty
        if self.resultText.get(1.0, tk.END) != "":
            text = self.sampleText.get(1.0, tk.END)
            self.executeOnText(lambda: self.resultText.delete(1.0, tk.END))
            self.DfaStart(text)

    def fileButtonClicked(self):

        filetypes = (("text files", "*.txt"), ("All files", "*.*"))

        filename = fd.askopenfilename(
            title="Open a file", initialdir="./", filetypes=filetypes
        )
        if filename:

            # read file
            with open(filename, "r") as f:
                # read lines
                lines = f.readlines()
                # merge list to strings
                text = "".join(lines)

                def func():
                    self.sampleText.delete(1.0, tk.END)
                    self.resultText.delete(1.0, tk.END)
                    self.sampleText.insert(tk.END, text)

                self.executeOnText(func)
                self.DfaStart(text)

    def highlightText(self, text):
        self.resultText.tag_configure("highlight", background="yellow")
        highlightSwitch = False
        patternFound = []
        for char in text:
            if char == "<":
                highlightSwitch = True
                patternFound.append("")
            elif char == ">":
                highlightSwitch = False
            if char not in "<>":
                if highlightSwitch:
                    self.executeOnText(
                        lambda: self.resultText.insert(tk.END, char, ("highlight"))
                    )
                    patternFound[-1] += char
                else:
                    self.executeOnText(lambda: self.resultText.insert(tk.END, char))
        self.patternFoundCounter(patternFound)

    def patternFoundCounter(self, patternArray):
        for pattern in patternArray:
            if pattern in self.patternFound:
                self.patternFound[pattern] += 1
            else:
                self.patternFound[pattern] = 1

    def patternFoundPrint(self):
        self.infoText.tag_configure("important", background="red")
        self.executeOnInfoText(
            lambda: self.infoText.insert(tk.END, "Pattern Found:\n", ("important"))
        )
        self.infoText.tag_configure("patternFound", background="#90ee90")
        for key, value in self.patternFound.items():
            self.executeOnInfoText(
                lambda: self.infoText.insert(
                    tk.END, key + " : " + str(value) + "\n", ("patternFound")
                )
            )

    def DfaStart(self, text):
        self.patternFound = {}
        stack = self.DfaInput(text)
        if stack[-1] != "" or len(stack) > 1:
            self.highlightText("".join(stack))
        self.patternFoundPrint()

    def DfaInput(self, text):
        self.t.initializeSearch()

        stack = [""]
        for char in text:
            # char = text[pIndex]
            stateOfDfa = self.t.insertNextChar(char)
            stack[-1] += char
            if stateOfDfa is None and char in self.seperatorChar:
                if len(stack) > 1:
                    if stack[1][0] not in self.seperatorChar and stack[0][-1] != " ":
                        stack[0] = stack[0].strip("<>") + stack[1]
                        stack.pop(1)
                self.highlightText(stack[0])
                stack.pop(0)
                stack = self.DfaInput("".join(stack))

            elif stateOfDfa is True:
                if len(stack) == 1:
                    stack = ["<" + stack[-1] + ">", ""]
                else:
                    stack[0] = stack[0].strip("<>")
                    result = "<" + "".join(stack) + ">"
                    stack = [result, ""]
            elif stateOfDfa is False:
                if char in self.seperatorChar:
                    stack.append("")

        return stack


root = tk.Tk()
UI(root)
root.mainloop()
