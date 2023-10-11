#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
  int key;
  char info[10];
  struct node *left;
  struct node *right;
};

struct node *root;

struct node *insert_node(int x, char *s)
{
  struct node *q;
  q = (struct node *)malloc(sizeof(struct node));
  q->key = x;
  strcpy(q->info, s);
  q->left = NULL;
  q->right = NULL;
  return q;
}

void preorder(struct node *p)
{
  printf("%d %s\n", p->key, p->info);
  if (p->left != NULL) preorder(p->left);
  if (p->right != NULL) preorder(p->right);
}

struct city {
  int id;
  char name[10];
};

void construct_tree( )
{
  struct city ss[9] = {
    {5, "Otsu"},
    {3, "Osaka"},
    {1, "Kyoto"},
    {2, "Kobe"},
    {8, "Tokyo"},
    {6, "Sapporo"},
    {9, "Nagoya"},
    {7, "Yokohama"},
    {4, "Fukuoka"}
  };
  struct node *p;
  int i, x;
  char s[10];
  root = insert_node(ss[0].id, ss[0].name);
  for (i = 0; i < 8; i++) {
    x = ss[i+1].id;
    strcpy(s, ss[i+1].name);
    p = root;
    while (p != NULL){
      if ( x < p->key ) {
        if ( p->left != NULL ) p = p->left;
        else {
        p->left = insert_node( x, s );
        break;
        }
      } else if ( x > p->key ) {
        if ( p->right != NULL ) p = p->right;
        else {
          p->right = insert_node(x, s);
          break;
        }
      } else {
        printf("\n key %d: existing key \n", x);
        break;
      }
    }
  }
}

void search (int x)
{
  struct node *p;
  int v = 0;
  p = root;
  while ( p != NULL ) {
    if ( x == p->key ) {
      printf("%s\n", p->info );
      v = 1;
      break;
    }
    if ( x < p->key ) p = p->left;
    else p = p->right;
  }
  if ( v != 1 ) printf("not found\n");
}

int main( )
{
  int x;
  root = NULL;
  construct_tree( );
  printf("\n");
  preorder(root);
  printf("\n");
  printf("search data of key value %d\n", 7);
  x = 7;
  search(x);
  printf("\n");
  printf("search data of key value %d\n", 10);
  x = 10;
  search(x);
}
