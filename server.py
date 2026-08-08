from src.main import create_mcp

app = create_mcp().http_app(transport='streamable-http')
