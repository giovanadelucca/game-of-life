# -*- coding: utf-8 -*-

"""
Criado em 04/01/2015
@author: Nicoli Araújo
@author: Elloá B. Guedes


Este módulo contém as classes que definem um Autômato Celular.
Superclasse CellularAutomata - Define métodos e atributos gerais de um CA
Classe ElementaryCode - Instancia métodos e atributos específicos para autômatos celulares com k = 2
Classe TotalisticCode - Instancia métodos e atributos para autômatos celulares com k > 2 
"""

from __future__ import unicode_literals

from IntKBase import IntKBase


class CellularAutomata(object):
    
    """
    SuperClasse que define autômatos celulares. 
    Um automato celular é um vetor multidimensional composto por células que detém um estado. 
    O estado de cada célula é determinado por uma regra numérica que considera os estados das celulas vizinhas. 
    """

    def __init__(self, neighborhood, rule, k, seed):
        
        """
        Construtor do autômato celular.
        Aqui, são instanciados a regra (rule), o número de estados(k), e o primeiro estado da célula 
        que se encontra exatamente no centro do vetor (seed). Após isso, é criado um dicionário que 
        associa o estado da vizinhança de uma célula com o seu próprio (dictRule).
        -rule (int) : número da regra a que o autômato obedece.
        -k (int) : número de estados que cada célula do autômato pode ter. Os estados são inteiros de 0 a k - 1.
        -seed (int) : estado inicial da célula central do autômato celular
        
        Após isso, é criado um dicionário que associa o estado da vizinhança de uma célula com o seu próprio (dictRule).
        -dictRule ( dict (int -> int) ) :  dicionário que relaciona os estados de uma vizinhança (inteiros de 0 a 7) 
        ao estado de uma célula (bits de rule na base k).                                 
        -type (str) : tipo do autômato celular. Inicialmente, é vazio, ou genérico.
        """
        
        self.__neighborhood = neighborhood
        self.__rule = rule
        self.__k = k
        self.__seed = seed
        self.__catype = ''

        self.__dictRule = self.setDictRule(self.neighborhood, self.rule, self.k)
    

        
    def setDictRule(self, neighborhood, rule, k):
        
        """
        Cria o dicionário de 8 chaves dictRule, que relaciona a vizinhança com o estado de uma célula.
        Cada chave é um inteiro de 0 a 7 que representa uma soma dos estados de uma vizinhança. 
        As chaves guardam inteiros que vão de 0 a k-1, que representam os possíveis estados da 
        célula a partir da vizinhança designada na chave. Cada estado é um bit da string de tamanho 
        8 ruleInKBase. É nesta variável que rule escrita na base k é guardada.
        Retorna dictRule (int -> int)
        >>> ca.setDictRule(30, 2)
        {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0}
        >>> ca.setDictRule(45, 3)
        {0: 0, 1: 0, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0}
        >>> ca.setDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
        """
        
        ruleInKBase = IntKBase(rule, k).numInBase
        self.__dictRule = {}
        numComb = self.k**neighborhood #o número de combinações de estados de um automato é igual ao numero de estados elevado ao cubo
        if (len(ruleInKBase) < numComb):
            while (len(ruleInKBase) < numComb):
                ruleInKBase = "0" + ruleInKBase 
        
        i = numComb-1
        for d in ruleInKBase:
            self.__dictRule[i] = int(d)
            i -=1
        return self.__dictRule
    
    
    def getNext(self, b1, b2, b3):     
        pass
    

    def __str__(self):
        
        """
        Retorna o nome do autômato celular.
        """
        
        return str(self.type) + str(self.rule)
    
    
    def getState(self, chave):
        
        """
        Retorna dictRule[chave].
        chave (int) - um inteiro de 0 a 7, que armazena uma das oito possíveis combinações de 
        estados da vizinhança de uma célula. 
        >>> ca.setDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
        ca.getState(0)
        2
        ca.getState(6)
        0
        ca.getState(4)
        2
        """
        
        return self.dictRule[chave]
    
    @property
    def neighborhood(self):
        return self.__neighborhood
    
    @property
    def rule(self):
        return self.__rule
    
    @property
    def k(self):
        
        """
        Retorna k.
        """
        
        return self.__k
    
    @property
    def dictRule(self):
        return self.__dictRule
    
    @property
    def catype(self):
        return self.__catype
    
    @catype.setter
    def catype(self, catype):
        self.__catype = catype
        
    @property
    def seed(self):
        return self.__seed    