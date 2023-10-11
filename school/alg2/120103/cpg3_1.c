#include <stdio.h>
#include <stdlib.h>

struct node *root;
struct node{
  char data;
  struct node *left;
  struct node *right;
};

void preorder(struct node *p)
{
  printf("%c\n", p->data);
  if (p->left != NULL) preorder(p->left);
  if (p->right != NULL) preorder(p->right);
}

void inorder(struct node *p)
{
  if (p->left != NULL) inorder(p->left);
  printf("%c\n", p->data);
  if (p->right != NULL) inorder(p->right);
}

void postorder(struct node *p)
{
  if (p->left != NULL) postorder(p->left);
  if (p->right != NULL) postorder(p->right);
  printf("%c\n", p->data);
}

struct node *insert_node(char x)
{
  struct node *q;
  q = (struct node *)malloc(sizeof(struct node));
  q->data = x;
  q->left = NULL;
  q->right = NULL;
  return q;
}

int main( )
{
  root = insert_node('A');
  root->left = insert_node('B');
  root->left->left = insert_node('D');
  root->left->right = insert_node('E');
  root->left->right->left = insert_node('H');
  root->right = insert_node('C');
  root->right->left = insert_node('F');
  root->right->right = insert_node('G');
  root->right->right->left = insert_node('I');
  printf("\n");
  preorder(root);
  printf("\n");
  inorder(root);
  printf("\n");
  postorder(root);
}
