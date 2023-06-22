# Autogenerated file
def render(v_old,vramp_old,i_old,call_conn, call_HV, call_v, call_ramp, call_i):
    yield """<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"UTF-8\">
        <title>Pico W</title>
    </head>
    <body>
        <h1>Pico W</h1>
        <h2>Set and Enable HV Output</h2>
        <p>Control HV Status</p>
        <a href=\led=on><button>ON</button></a>&nbsp;
        <a href=\led=off><button>OFF</button></a>

        <form action=\"\", method=\"post\">
             <p>Output Voltag:</p>
             <p><input type=\"text\" id=\"bz\" name =\"v_out\"> | last selected """
    yield str(v_old)
    yield """ [V]</p>

             <p>Rampup Speed:</p>
             <p><input type=\"text\" id=\"bt\" name =\"vramp_out\"> | last selected """
    yield str(vramp_old)
    yield """ [V/s] </p>
             
             <p>Current Maximum:</p>
             <p><input type=\"text\" id=\"bt\" name =\"i_out\"> | last selected """
    yield str(i_old)
    yield """ [mA] </p>

             <p><input type=\"submit\" name=\"submit_button\" value=\"Submit!\"></p>


        </form>
        
        <h2>HV Output Status</h2>
        
        <form action=\"\", method=\"post\">
        
             <p>Connection: """
    yield str(call_conn)
    yield """</p> 
             <p>HV: """
    yield str(call_HV)
    yield """</p> 
             <p>Voltage:"""
    yield str(call_v)
    yield """ [V] </p> 
             <p>Ramp-up: """
    yield str(call_ramp)
    yield """ [V/s]</p> 
             <p>Current: """
    yield str(call_i)
    yield """ [mA]</p> 
             
             


             <p><input type=\"submit\" name=\"load_button\" value=\"Call Device\"></p>


        </form>
        
        <h2>Data Logs</h2>
        <a href=\download target=\"_blank\">Download most recent Log</a>

        <script>
        </script>
    </body>
</html>

"""