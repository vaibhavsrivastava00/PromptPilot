import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    const disposable = vscode.commands.registerCommand('task-executor.runAgent', async () => {
        const task = await vscode.window.showInputBox({
            prompt: 'Enter the task you want the AI to execute',
            placeHolder: 'e.g., Create a git repo and push code'
        });
        if (!task?.trim()) {
            vscode.window.showErrorMessage('⚠️ Task description is required!');
            return;
        }
        

        const pythonScriptPath = path.join(context.extensionPath, 'AI_AGENT', 'agent.py');
        const terminal = vscode.window.createTerminal('AI Agent');
        terminal.sendText(`cd "${path.dirname(pythonScriptPath)}"`);
        terminal.sendText(`python "${pythonScriptPath}" "${task}"`);
        vscode.window.showInformationMessage(`Task "${task}" sent to AI agent. Output is in terminal.`);
        terminal.show();
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
