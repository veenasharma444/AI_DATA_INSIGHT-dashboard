from dash import Input, Output, State, callback
import dash
from core import db_connector
from sqlalchemy import text


@callback(
    Output('db-connection-status', 'children'),  # ✅ FIXED TARGET
    Output('db-table-section', 'style'),  # ✅ ADD THIS
    Input('btn-test-db', 'n_clicks'),
    State('db-type-dropdown', 'value'),
    State('db-host', 'value'),
    State('db-port', 'value'),
    State('db-name', 'value'),
    State('db-username', 'value'),
    State('db-password', 'value'),
    prevent_initial_call=True
)
def test_db_connection(n_clicks, db_type, host, port, db_name, username, password):

    if not n_clicks:
        raise dash.exceptions.PreventUpdate

    try:
        #  connect
        engine = db_connector.connect(
            db_type,
            host,
            port,
            db_name,     # ✅ correct
            username,    # ✅ correct
            password
        )

        #  test
        conn = engine.connect()
        conn.execute(text("SELECT 1"))
        conn.close()

        return " Connection successful", {'display': 'block'}

    except Exception as e:
        return f" Connection failed: {str(e)[:100]}", {'display': 'none'}
