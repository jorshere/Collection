package project.ChatBox;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {         // listen to new clients, wants to connect & spwan thread to handle it.

    private ServerSocket serverSocket;  //this object is responsible for listing to incomming
                                        // connection or clients and create a socket object for communication.

    public Server(ServerSocket serverSocket) {
        this.serverSocket = serverSocket;
    }

    public void startServer(){          // responsible for keep our servers running

        try{
            while(!serverSocket.isClosed()){

                Socket socket = serverSocket.accept();
                /* this is a blocking method, our program will be in halt until a client connect; however when the
                client does connect a socket object is returned to communicate with the client;
                 */

                System.out.println("A new client has connected !!");
                ClientHandler clientHandler = new ClientHandler(socket);  // used to handle multiple connection or as needed;

                Thread thread = new Thread(clientHandler);
                thread.start();
            }
        } catch (IOException e){

        }
    }

    public void closeServerSocket(){    // to close the server socket.
        try{
            if(serverSocket != null){
                serverSocket.close();
            }
        }catch (IOException e){
            e.printStackTrace();            // used to handle exceptions and errors.
        }

    }
    public static void main(String [] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(1234);
        Server server=new Server(serverSocket);
        server.startServer();      // to keep our server constantly running;
    }
}
