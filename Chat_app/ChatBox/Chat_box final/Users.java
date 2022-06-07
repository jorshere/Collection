package com.Passion;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Users extends JFrame implements ActionListener, Runnable{

    static  JPanel jPanel;
    static JTextField jTextField,jTextField2;
    static JButton jButton,jButton2;
    public static JTextArea jTextArea;
    String user1="";




    BufferedWriter writer;
    BufferedReader reader;

    Users(){
        Scanner sc = new Scanner(System.in);
        user1 = sc.nextLine();

        jPanel = new JPanel();
        jPanel.setLayout(null);
        jPanel.setBackground(new Color(70,130,180));
        jPanel.setBounds(0,0,360,50);
        add(jPanel);

        ImageIcon imageIcon = new ImageIcon(ClassLoader.getSystemResource("com/Passion/3.png"));
        Image image1 = imageIcon.getImage().getScaledInstance(35,35,Image.SCALE_DEFAULT);
        ImageIcon imageIcon1 = new ImageIcon(image1);
        JLabel jLabel1 = new JLabel(imageIcon1);
        jLabel1.setBounds(5,6,35,35);
        jPanel.add(jLabel1);

        jLabel1.addMouseListener(new MouseAdapter(){
            public void mouseClicked(MouseEvent ae){
                System.exit(0);
            }
        });

        jTextArea = new JTextArea();
        jTextArea.setBounds(5,55,324,450);
        jTextArea.setBackground(new Color(176,224,230));
        jTextArea.setFont(new Font("SAN SERIF", Font.BOLD,16));
        jTextArea.setEditable(false);
        jTextArea.setLineWrap(true);
        jTextArea.setWrapStyleWord(true);
        add(jTextArea);



        jTextField = new JTextField();
        jTextField.setBounds(5,515,250,40);
        jTextField.setFont(new Font("SAN_SARIF",Font.PLAIN,15));
        add(jTextField);

        jButton = new JButton("Send");
        jButton.setBounds(260,515,70,40);
        jButton.setBackground(new Color(70,130,180));
        jButton.setForeground(Color.WHITE);
        jButton.setFont(new Font("SAN_SARIF",Font.BOLD,12));
        jButton.addActionListener(this);
        add(jButton);


        JLabel jLabel2 = new JLabel(user1);
        jLabel2.setFont(new Font("SAN_SARIF",Font.BOLD,15));
        jLabel2.setForeground(Color.WHITE);
        jLabel2.setBounds(45,16,100,20);
        jPanel.add(jLabel2);


        getContentPane().setBackground(new Color(95,158,160));
        setLayout(null);
        setSize(350,600);
        setLocationRelativeTo(null);
        setUndecorated(false);
        setVisible(true);

        try{

            Socket socketClient = new Socket("localhost", 2003);
            writer = new BufferedWriter(new OutputStreamWriter(socketClient.getOutputStream()));
            reader = new BufferedReader(new InputStreamReader(socketClient.getInputStream()));
        }catch(Exception e){}

    }

    public void actionPerformed(ActionEvent ae){
        String str =user1+": "+jTextField.getText();
        try{
            writer.write(str);
            writer.write("\r\n");
            writer.flush();
        }catch(Exception e){}
        jTextField.setText("");
    }

    public void run(){
        try{
            String msg = "";
            while((msg = reader.readLine()) != null){
                jTextArea.append(msg + "\n");
            }
        }catch(Exception e){}
    }

    public static void main(String[] args){

        System.out.println("enter name:  ");


        Users one = new Users();
        Thread t1 = new Thread(one);
        t1.start();
    }

}
