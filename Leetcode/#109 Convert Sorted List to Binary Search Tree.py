# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:48:51 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        
        def converter(lst1):
            
            if lst1 == []:
                return None
                exit
                
            l = (len(lst1)-1)//2            
            root = TreeNode(lst1[l])
            root.left = converter(lst1[:l])
            root.right = converter(lst1[l+1:])
            return root
        
        return converter(lst)