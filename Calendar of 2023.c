
#include<stdio.h>
void month();
void days_name(int p);
void no_days(int a);
int x,count=0;

void month()
{
	for(int i=1;i<=12;i++)
    {	
		switch (i)
        {
			case 1:
			printf("\n\t  ---JANUARY---");
            break;
            case 2:printf("\n\n\t  ---FEBRUARY---");
            break;
            case 3:printf("\n\n\t  ---MARCH---");
            break;
            case 4:printf("\n\n\t  ---APRIL---");
            break;
            case 5:printf("\n\n\t  ---MAY---");
            break;
            case 6:printf("\n\n\t  ---JUNE---");
            break;
            case 7:printf("\n\n\t  ---JULY---");
            break;
            case 8:printf("\n\n\t  ---AUGUST---");
            break;
            case 9:printf("\n\n\t  ---SEPTEMBER---");
            break;
            case 10:printf("\n\n\t  ---OCTOBER---");
            break;
            case 11:printf("\n\n\t  ---NOVEMBER---");
            break;
            case 12:printf("\n\n\t  ---DECEMBER---");
            break;
        }
		days_name(i);
    }
}

void days_name(int p)
{
	char days[]="SUN  MON  TUE  WED  THU  FRI  SAT";
	printf("\n\n%s\n---------------------------------\n",days);
	no_days(p);
    //printf("\n(days_name)x=%d\n",x);
}
void no_days(int a)
{
	int i,j=31;
    if(count=1)
    {
		for(count;count<=x;count++)
        {
			printf(" ");
        }
    }    
    if(a==2)
		j=28;
    //else if(a==2&&mod==0)    
	//j=29;
    else if(a==4||a==6||a==9||a==11)   
		j=30;
    //printf("\nstart of days :x=%d\n",x);    
    for(i=1,x;i<=j;x++)     
    {   
		if(i<=9)
        {
			if(x==1||x==6||x==11||x==16||x==21||x==26||x==31)
			{
				printf(" %d",i);
				i++;
			}    
	 		else if(x==2||x==3||x==4||x==7||x==8||x==9||x==12||x==13||x==14||x==17||x==18||x==19||x==22||x==23||x==24||x==27||x==28||x==29)
				printf(" ");
	 		else if(x==32)   
			{
				printf("\n");
	    		x=0;
	 		}    
        }
        else
        {	
			if(x==1||x==6||x==11||x==16||x==21||x==26||x==31)
			{
				printf("%d",i);
				i++;
			}    
	 		else if(x==0||x==2||x==9||x==10||x==13||x==17||x==18||x==23||x==28||x==29)
				printf("  ");
	 		else if(x==32)   
			{
				printf("\n ");
	    		x=0;
	 		}    
        }

    }
    count=1;
 }
void main ()
{
printf("\t---CALANDER-2023---\n");
	month();
}
