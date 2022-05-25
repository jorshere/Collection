package project.ChatBox;

import java.io.*;
import java.net.Socket;
import java.util.ArrayList;

public class ClientHandler implements Runnable {   //so that the instances will be executed by separate thread

    public static ArrayList<ClientHandler> clientHandlers = new ArrayList<>();
    /* to keep track of every client; responsible for communicating with multiple client*/

    private Socket socket;                      // used to connect between client and server;
    private BufferedReader bufferedReader;                // used to read data; msg sent from client;
    private BufferedWriter bufferedWriter;         // used to send data; msg to a client;
    private String clientUsername;             // to represent each client;

    public ClientHandler(Socket socket) {
        try {
            this.socket = socket;
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        /* [OutputStreamWriter] we are wrapping the byte stream to a character stream
         because we want to send over character
         */
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.clientUsername = bufferedReader.readLine();
            clientHandlers.add(this);
            broadcastMessage("SERVER : " + clientUsername + " has entered the chat");
        } catch (IOException e) {
            closeEverything(socket, bufferedWriter, bufferedReader); // to close everything
        }

    }

    @Override                                  //  for execution in separate thread  we need to override this method.
    public void run() {
        String messageFromClient;  // to hold the msg

        while(socket.isConnected()){
            try{
                messageFromClient=bufferedReader.readLine();
    /* [messageFromClient=bufferedReader.readLine()]   while the socket is connected , we are going to read msg from
    the bufferreader; basically the program will halt here until we receive the msg; and this is why
    we have to run it on a seperate thread;
     */
                broadcastMessage(messageFromClient);
            }catch(IOException e){
                closeEverything(socket, bufferedWriter,bufferedReader);
                break;
            }

        }
    }
    public void broadcastMessage(String messageToSent){
        for(ClientHandler clientHandler:clientHandlers){
            try{                            //we dont want msg to be sent to the same person who sent it;
                if(!clientHandler.clientUsername.equals(clientUsername)){
                    clientHandler.bufferedWriter.write(messageToSent);
                    clientHandler.bufferedWriter.newLine();
                    clientHandler.bufferedWriter.flush();
                }
            }catch(IOException e){
                closeEverything(socket, bufferedWriter,bufferedReader);
            }
        }
    }
    public void removeClientHandler(){
        clientHandlers.remove(this);  // first to remove that client when he lefts;
        broadcastMessage("SERVER "+clientUsername+" has left chat");
    }
    public void closeEverything(Socket socket, BufferedWriter bufferedWriter, BufferedReader bufferedReader){
        removeClientHandler();
        try{
            if(bufferedReader!= null){
                bufferedReader.close();
            }
            if(bufferedWriter != null){
                bufferedWriter.close();
            }
            if(socket != null){
                socket.close();
            }
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
