#include <stdio.h>
#include <string.h>

struct Contact { char name[50], email[50]; long long phone; int age; } c[100];
int total = 0;

int find(char* n) {
    for(int i = 0; i < total; i++) if(strcmp(c[i].name, n) == 0) return i;
    return -1;
}

int main() {
    char ch[5], n[50];
    while(printf("\n1.Add 2.View 3.Update 4.Del 5.Search 6.Count 7.Exit\nOption: ") && scanf("%s", ch) && ch[0]!='7') {
        int idx = -1;
        if(ch[0] == '1' || ch[0] == '3' || ch[0] == '4' || ch[0] == '5') {
            printf("Enter name: "); scanf("%s", n); idx = find(n);
        }
        
        if(ch[0]=='1') {
            if(idx != -1) printf("Exists.\n");
            else { 
                strcpy(c[total].name, n);
                printf("Enter phone: "); scanf("%lld", &c[total].phone);
                printf("Enter email: "); scanf("%s", c[total].email);
                printf("Enter age: ");   scanf("%d", &c[total].age);
                if(c[total].age < 0) printf("Negative age!\n"); else total++;
            }
        }
        else if(ch[0]=='2') {
            for(int i = 0; i < total; i++) printf("%s %lld %s %d\n", c[i].name, c[i].phone, c[i].email, c[i].age);
            if(total == 0) printf("No contacts.\n");
        }
        else if(ch[0]=='3') {
            if(idx == -1) printf("Not found.\n");
            else { 
                printf("New phone: "); scanf("%lld", &c[idx].phone);
                printf("New email: "); scanf("%s", c[idx].email);
                printf("New age: ");   scanf("%d", &c[idx].age); 
            }
        }
        else if(ch[0]=='4') {
            if(idx == -1) printf("Not found.\n"); 
            else { c[idx] = c[--total]; printf("Deleted.\n"); }
        }
        else if(ch[0]=='5') {
            if(idx == -1) printf("Not found.\n"); 
            else printf("Name: %s Phone: %lld Email: %s Age: %d\n", c[idx].name, c[idx].phone, c[idx].email, c[idx].age);
        }
        else if(ch[0]=='6') printf("Total contacts: %d\n", total);
    }
    return 0;
}
