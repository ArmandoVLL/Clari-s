from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Usuario')
def Usuario():    
    return render_template('log_in_usuario.html')

@app.route('/Admin')
def Invitado():
    return render_template('register_inivitado.html')

if __name__ == '__main__':
    app.run(debug=True)

"""   <script>
        document.getElementById("showInterfaceBtn").addEventListener("click", function() {
            document.getElementById("interfaceContainer").classList.remove("hidden");
            document.getElementById("welcomeMessage").style.display = "none";
            this.style.display = "none"; // Ocultar el botón después de mostrar la interfaz
        });

        document.getElementById("backBtn").addEventListener("click", function() {
            document.getElementById("interfaceContainer").classList.add("hidden");
            document.getElementById("welcomeMessage").style.display = "block";
            document.getElementById("showInterfaceBtn").style.display = "block"; // Mostrar el botón inicial de nuevo
        });
    </script>
    """
 
 
