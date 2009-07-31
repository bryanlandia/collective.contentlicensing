##################################################################################
#    Copyright (c) 2004-2009 Utah State University, All rights reserved.
#    Portions copyright 2009 Massachusetts Institute of Technology, All rights reserved.
#                                                                                 
#    This program is free software; you can redistribute it and/or modify         
#    it under the terms of the GNU General Public License as published by         
#    the Free Software Foundation, version 2.                                      
#                                                                                 
#    This program is distributed in the hope that it will be useful,              
#    but WITHOUT ANY WARRANTY; without even the implied warranty of               
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                
#    GNU General Public License for more details.                                 
#                                                                                 
#    You should have received a copy of the GNU General Public License            
#    along with this program; if not, write to the Free Software                  
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA    
#                                                                                 
##################################################################################

__author__  = '''Brent Lambert, David Ray, Jon Thomas'''
__docformat__ = 'plaintext'
__version__   = '$ Revision 0.0 $'[11:-2]

from zope.interface import Interface
from zope.annotation.interfaces import IAnnotatable

class ILicensable(IAnnotatable):
    """ Marker interface """

class ILicense(Interface):
    """ License interface """

    def getRightsLicense():
        """ Get the license """
        
    def setRightsLicense(ldata):
        """ Set the license """

    def getRightsHolder():
        """ Get the contents of the DC.rightsHolder field. """

    def setRightsHolder(rhdata):
        """ Set the DC.rightsHolder field. """

        
