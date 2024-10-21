from pygls.server import LanguageServer # Handles communication between server and vsc
from pygls.lsp.types import CompletionItem, CompletionItemKind, CompletionParams # presents a single suggestion in the completion list // Specifies the kind of item being suggested( Keyword, Function, Variable)

# Basic keywords (will expand later)
SURICATA_KEYWORDS = ["alert", "drop", "pass", "reject", "log", "msg", "sid", "flow"]

# Server (will handle requests from the client (vsc) and provide responses (like autocompletions)
server = LanguageServer()

# This registers the function as a handler for the 
@server.feature('textDocument/completion')
def completions(ls: LanguageServer, params: CompletionParams):
    """Provide basic completion"""
    return [
        CompletionItem(label=kw, kind=CompletionItemKind.Keyword)
        for kw in SURICATA_KEYWORDS
    ]

if __name__ == '__main__':
    server.start_io()
