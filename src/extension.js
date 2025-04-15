"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const path = __importStar(require("path"));
function activate(context) {
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
function deactivate() { }
//# sourceMappingURL=extension.js.map