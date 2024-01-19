//package org.example;
import java.awt.*;
import java.awt.event.*;
public class Calculator_app extends Frame implements ActionListener{
    String val="";
    int check=0,n;
    public double[] num=new double[2];
    int i=0;
    String pros;
    Label l1;
    TextField t=new TextField("0");
    Button b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,ba,bs,bm,bd,be,clr,del;
    Menu m=new Menu("Menu");
    MenuBar mb=new MenuBar();
    MenuItem i1,i2;
    Font fnt=new Font("Courier",Font.BOLD,16);
    public Calculator_app()
    {
        b0=new Button("0");
        b1=new Button("1");
        b2=new Button("2");
        b3=new Button("3");
        b4=new Button("4");
        b5=new Button("5");
        b6=new Button("6");
        b7=new Button("7");
        b8=new Button("8");
        b9=new Button("9");
        ba=new Button("+");
        bs=new Button("-");
        bm=new Button("x");
        bd=new Button("/");
        be=new Button("=");
        clr =new Button("AC");
        del =new Button("Del");
        i1=new MenuItem("Scientific");
        i2=new MenuItem("Quit");
        i2.addActionListener((event) -> System.exit(0));
        l1=new Label("CALCULATOR");

        l1.setFont(fnt);
        t.setFont(fnt);
        l1.setBounds(60,60,120,18);
        t.setBounds(15,100,205,35);
        b9.setBounds(100,150,35,35);
        b8.setBounds(60,150,35,35);
        b7.setBounds(20,150,35,35);
        b6.setBounds(100,190,35,35);
        b5.setBounds(60,190,35,35);
        b4.setBounds(20,190,35,35);
        b3.setBounds(100,230,35,35);
        b2.setBounds(60,230,35,35);
        b1.setBounds(20,230,35,35);
        b0.setBounds(25,270,105,35);
        ba.setBounds(140,150,35,35);
        bs.setBounds(140,190,35,35);
        bm.setBounds(140,230,35,35);
        bd.setBounds(140,270,35,35);
        clr.setBounds(180,150,35,55);
        del.setBounds(180,210,35,55);
        be.setBounds(180,270,35,35);

        m.add(i1);
        m.add(i2);
        mb.add(m);
        setMenuBar(mb);
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
        add(ba);
        add(bs);
        add(bm);
        add(bd);
        add(clr);
        add(del);
        add(be);
        add(new Canva());

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

//        pack();
        setTitle("CALCULATOR");
        setSize(235,360);
        setLayout(null);
        setVisible(true);
        l1.setBackground(Color.black);
        l1.setForeground(Color.white);
    }
    public void actionPerformed(ActionEvent e){
        if (e.getSource()==be) {
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
        } else if (e.getSource()==del) {
            if(val.endsWith("+") || val.endsWith("-") || val.endsWith("x") || val.endsWith("/")){
                pros="";
                check=0;
            }
            else{
                num[i] = (int) (num[i]/10.0);
            }
            val=val.substring(0,(val.length())-1);
            t.setText(val);

        } else if (e.getSource()==clr) {
            val="";
            num[0]=0;
            num[1]=0;
            check=0;
            t.setText(val);

        } else if (e.getSource()==ba ) {
            if(check!=1){
                pros="add";
                val+="+";
                i=1;
                check=1;
                t.setText(val);
            }
            else{
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } else if (e.getSource()==bs) {
            if(check!=1) {
                pros = "sub";
                val += "-";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else{
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } else if (e.getSource()==bm) {
            if(check!=1) {
                pros = "mul";
                val += "x";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else{
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        } else if (e.getSource()==bd) {
            if(check!=1) {
                pros = "div";
                val += "/";
                i = 1;
                check = 1;
                t.setText(val);
            }
            else{
                t.setText("One Operation can do!");
                i=0;
                num[0]=0;
                num[1]=0;
                val="";
                check=0;
            }
        }
    }
    public void action(int number,Button obj)
    {
        obj.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                n=number;
                val+=Integer.toString(number);
                num[i]*=10;
                num[i]+=number;
                t.setText(val);
            }
        });
    }

    public static void main(String[] args)
    {
        Calculator_app c=new Calculator_app();
    }
}
class Canva extends Canvas
{
    public Canva()
    {
        setBackground(Color.black);
        setSize(400,400);
    }
}
