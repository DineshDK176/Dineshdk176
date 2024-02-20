//package org.example;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
class Calculator extends JFrame implements ActionListener
{
    String val = "";
    int check = 0 , n ; //check  --> Check number of Operations
    public double[] num = new double[2];
    int i = 0; //Index Value of num Array.
    String pros;
    Label l1;
    JTextField t = new JTextField("0");
    JButton b0 , b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8, b9 , dot , ba , bs , bm , bd , be , clr , del;
    JMenu m= new JMenu("Menu");
    JMenuBar mb = new JMenuBar();
    JMenuItem  i1;
    Font fnt = new Font("Courier",Font.BOLD,16);
    Calculator()
    {
        b0 = new JButton("0");
        b1 = new JButton("1");
        b2 = new JButton("2");
        b3 = new JButton("3");
        b4 = new JButton("4");
        b5 = new JButton("5");
        b6 = new JButton("6");
        b7 = new JButton("7");
        b8 = new JButton("8");
        b9 = new JButton("9");
        dot = new JButton(".");
        ba = new JButton("+");
        bs = new JButton("-");
        bm = new JButton("x");
        bd = new JButton("/");
        be = new JButton("=");
        clr = new JButton("AC");
        del = new JButton("DL");
        i1= new JMenuItem("Quit");
        i1.addActionListener((event) -> System.exit(0));
        l1 = new Label("CALCULATOR");

        l1.setFont(fnt);
        l1.setBackground(Color.black);
        l1.setForeground(Color.white);
        t.setFont(fnt);
        l1.setBounds(80,10,135,35);
        t.setBounds(25,60,235,35);
        b9.setBounds(120,120,50,35);
        b8.setBounds(65,120,50,35);
        b7.setBounds(10,120,50,35);
        b6.setBounds(120,160,50,35);
        b5.setBounds(65,160,50,35);
        b4.setBounds(10,160,50,35);
        b3.setBounds(120,200,50,35);
        b2.setBounds(65,200,50,35);
        b1.setBounds(10,200,50,35);
        b0.setBounds(10,240,105,35);
        dot.setBounds(120,240,50,35);
        ba.setBounds(175,120,50,35);
        bs.setBounds(175,160,50,35);
        bm.setBounds(175,200,50,35);
        bd.setBounds(175,240,50,35);
        clr.setBounds(230,120,50,55);
        del.setBounds(230,180,50,55);
        be.setBounds(230,240,50,35);

        m.add(i1);
        mb.add(m);
        setJMenuBar(mb);
        add(l1);
        add(t);
        add(b9);
        add(b8);
        add(b7);
        add(b6);
        add(b5);
        add(b4);
        add(b3);
        add(b2);
        add(b1);
        add(b0);
        add(dot);
        add(ba);
        add(bs);
        add(bm);
        add(bd);
        add(clr);
        add(del);
        add(be);
        add(new Canva());
        pack();

        action(0,b0);
        action(1,b1);
        action(2,b2);
        action(3,b3);
        action(4,b4);
        action(5,b5);
        action(6,b6);
        action(7,b7);
        action(8,b8);
        action(9,b9);
        be.addActionListener(this);
        del.addActionListener(this);
        clr.addActionListener(this);
        ba.addActionListener(this);
        bs.addActionListener(this);
        bm.addActionListener(this);
        bd.addActionListener(this);
 
        setTitle("CALCULATOR");
        setSize(300,400);
        setBackground(Color.black);
        setLayout(null);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e)
    {
        if (e.getSource()==be) 
        {
            double tot=switch (pros){
                case "add" -> num[0]+num[1];
                case "sub" -> num[0]-num[1];
                case "mul" -> num[0]*num[1];
                case "div" -> num[0]/num[1];
                default -> 0.0;
            };
            i=0;
            num[0]=0;
            num[1]=0;
            val=Double.toString(tot);
            t.setText(val);
            val="";
            check=0;
        } 
        else if (e.getSource()==del) 
        {
            if(val.endsWith("+") || val.endsWith("-") || val.endsWith("x") || val.endsWith("/"))
            {
                pros="";
                check=0;
            }
            else
            {
                num[i] = (int) (num[i]/10.0);
            }
            val=val.substring(0,(val.length())-1);
            t.setText(val);

        } 
        else if (e.getSource()==clr) 
        {
            num[0]*=0;
            num[1]*=0;
            check*=0;
            val="0";
            i=0;
            t.setText(val);
            val="";

        }
        else if (e.getSource()==ba ) 
        {
            if(check!=1)
            {
                pros="add";
                val+="+";
                i=1;
                check=1;
                t.setText(val);
            }
            else
            {
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } 
        else if (e.getSource()==bs) 
        {
            if(check!=1) 
            {
                pros = "sub";
                val += "-";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else
            {
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } 
        else if (e.getSource()==bm) 
        {
            if(check!=1) 
            {
                pros = "mul";
                val += "x";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else
            {
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } 
        else if (e.getSource()==bd) 
        {
            if(check!=1) 
            {
                pros = "div";
                val += "/";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else
            {
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        }
    }
    public void action(int number,JButton obj)
    {
        obj.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
                n=number;
                val+=Integer.toString(number);
                num[i]*=10;
                num[i]+=number;
                t.setText(val);
            }
        });
    }
}

public class Calculator_app {
    public static void main(String[] args)
    {
        Calculator c=new Calculator();
    }
}

class Canva extends Canvas
{
    public Canva()
    {
        setBackground(Color.black);
        setSize(1200,1000);
    }
}
