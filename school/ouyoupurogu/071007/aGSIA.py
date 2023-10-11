#-*- coding: utf-8-*-

from xml.etree import ElementTree               # XML-parser

from matplotlib.patches import PathPatch

from matplotlib.path import Path

import numpy as np

import os, pathlib



topdir = './GSI/'



def readDEM5 (filename, dir=topdir, debug=0):

  path = f'{dir}{filename[:14]}{filename[17:23]}/{filename}.xml'

  try:

    root = ElementTree.parse (path).getroot ()

    for son in root.iter ():

      if   'high'       in son.tag: size = list (map (int, son.text.split ()))

      elif 'startPoint' in son.tag: start = list (map (int, son.text.split ()))

      elif 'tupleList'  in son.tag: elev = son.text

    size[0] += 1; size[1] += 1

    st = start[0]+start[1]*size[0]

    ret = np.full (size[0]*size[1], np.nan)

    val = np.asarray (list (map (float, elev

      .replace ('表層面,', '').replace ('地表面,', '')

      .replace ('海水面,', '').replace ('内水面,', '')

      .replace ('データなし,', '').replace ('その他,', '')

      .replace ('-9999.', 'NaN').strip ().splitlines ())))

    ret[st:st+val.size] = val

    if debug > 1: print ('reading', filename, st, val.size)

    return ret.reshape ((size[1], size[0]))

  except FileNotFoundError:

    if debug > 0: print ('reading', filename, ': not found')

    return np.full ([150, 225], np.nan)



def readDEM10 (filename, dir=topdir, encoding='utf-8', debug=0):

  path = f'{dir}{filename[:11]}/{filename}.xml'

  try:

    f = open (path, encoding=encoding)

    root = ElementTree.fromstring (f.read ())

    for son in root.iter ():

      if   'high'       in son.tag: size = list (map (int, son.text.split ()))

      elif 'startPoint' in son.tag: start = list (map (int, son.text.split ()))

      elif 'tupleList'  in son.tag: elev = son.text

    size[0] += 1; size[1] += 1

    st = start[0]+start[1]*size[1]

    ret = np.full (size[0]*size[1], np.nan)

    val = np.asarray (list (map (float, elev

      .replace ('その他,', '').strip ().splitlines ())))

    ret[st:st+val.size] = val

    if debug > 1: print ('reading', filename, st, val.size)

    f.close ()

    return ret.reshape ((size[1], size[0]))

  except FileNotFoundError:

    if debug > 0: print ('reading', filename, ': not found')

    return np.full ([750, 1125], np.nan)



def readDEM (mesh, dir=topdir, date10='20161001', date5='20161001', debug=0):

  filename = f'FG-GML-{mesh[:4]}-{mesh[4:]}-dem10b-{date10}'

  elev10 = readDEM10 (filename, dir=dir, debug=debug)

  elev = np.repeat (np.repeat (elev10, 2, axis=1), 2, axis=0)

  A = np.empty ([10, 10], dtype=np.ndarray)

  B = np.empty ([10, 10], dtype=np.ndarray)

  C = np.empty ([10, 10], dtype=np.ndarray)

  for i in range (10):

    for j in range (10):

      filename = f'FG-GML-{mesh[:4]}-{mesh[4:]}-{i}{j}-DEM5A-{date5}'

      A[i, j] =  readDEM5 (filename, dir=dir, debug=debug)

      B[i, j] =  readDEM5 (filename.replace ('5A', '5B'), dir=dir, debug=debug)

      C[i, j] =  readDEM5 (filename.replace ('5A', '5C'), dir=dir, debug=debug)

  elevA = np.vstack (tuple (np.hstack (tuple (A[i, j] for j in range(10)))

    for i in reversed (range (10))))

  elevB = np.vstack (tuple (np.hstack (tuple (B[i, j] for j in range(10)))

    for i in reversed (range (10))))

  elevC = np.vstack (tuple (np.hstack (tuple (C[i, j] for j in range(10)))

    for i in reversed (range (10))))

  idx = np.zeros_like (elevA, dtype=np.int8)                         # 0: dem10

  idxC = ~np.isnan (elevC); idx[idxC] = 1; elev[idxC] = elevC[idxC]  # 1: DEM5C

  idxB = ~np.isnan (elevB); idx[idxB] = 2; elev[idxB] = elevB[idxB]  # 2: DEM5B

  idxA = ~np.isnan (elevA); idx[idxA] = 3; elev[idxA] = elevA[idxA]  # 3: DEM5A

  return elev, idx





def readPt (filename, dir=topdir, debug=0):

  ret = []

  pdir = ''

  if filename[0:7] == 'FG-GML-':

    sp = filename.split ('-')

    pdir = sp[0] + '-' + sp[1] + '-' + sp[2]

  if filename.endswith ('.xml'):

        files = pathlib.Path (dir + pdir).glob (filename)

  else: files = pathlib.Path (dir + pdir).glob (filename + '*.xml')

  for fname in files:

    if len (dir) == 0:

      f = open (fname, encoding='utf-8')

      root = ElementTree.fromstring (f.read ())

    elif len (pdir) == 9:

      f = open (fname, encoding='utf-8')

      root = ElementTree.fromstring (f.read ())

    else:

      root = ElementTree.parse (fname).getroot ()

    for son in root.iter ():

      if   'orgGILvl' in son.tag: level = int (son.text)

      elif 'pos' in son.tag:

        pos = list (map (float, son.text.split ()))

      elif 'text' in son.tag:

        text = son.text

      elif 'option' in son.tag:

        option = son.text

      elif 'type' in son.tag:

        ret.append ((pos, level, text,  option, son.text))

    if debug > 1: print ('reading', os.path.basename (fname), len(ret))

  else:

    if 'fname' not in locals ():

      if debug > 0: print ('not found:', os.path.basename (filename))

  return ret



def readLoc (filename, dir=topdir, debug=0):

  ret = []

  pdir = ''

  if filename[0:7] == 'FG-GML-':

    sp = filename.split ('-')

    pdir = sp[0] + '-' + sp[1] + '-' + sp[2]

  if filename.endswith ('.xml'):

        files = pathlib.Path (dir + pdir).glob (filename)

  else: files = pathlib.Path (dir + pdir).glob (filename + '*.xml')

  for fname in files:

    if len (dir) == 0:

      f = open (fname, encoding='utf-8')

      root = ElementTree.fromstring (f.read ())

    elif len (pdir) == 9:

      f = open (fname, encoding='utf-8')

      root = ElementTree.fromstring (f.read ())

    else:

      root = ElementTree.parse (fname).getroot ()

    for son in root.iter ():

      if   'orgGILvl' in son.tag: level = int (son.text)

      elif 'posList' in son.tag:

        pos = np.reshape (list (map (float, son.text.split ())), (-1, 2))

      elif 'type'    in son.tag:

        ret.append ((pos, level, son.text))

    if debug > 1: print ('reading', os.path.basename (fname), len(ret))

  else:

    if 'fname' not in locals ():

      if debug > 0: print ('not found:', os.path.basename (filename))

  return ret



def readArea (filename, dir=topdir, debug=0):

  ret = []

  pdir = ''

  if filename[0:7] == 'FG-GML-':

    sp = filename.split ('-')

    pdir = sp[0] + '-' + sp[1] + '-' + sp[2]

  files = pathlib.Path (dir + pdir).glob (filename + '*.xml')

  for fname in files:

    if len (pdir) == 9:

      f = open (fname, encoding='utf-8')

      root = ElementTree.fromstring (f.read ())

    else:

      root = ElementTree.parse (fname).getroot ()

    for son in root.iter ():

      if   'orgGILvl' in son.tag: level = int (son.text)

      elif 'exterior' in son.tag:

        exterior = True

        pos = []

      elif 'interior' in son.tag:

        exterior = False

      elif 'posList' in son.tag:

        pos.append (np.reshape (list (map (float, son.text.split ())), (-1, 2)))

      elif 'type'    in son.tag:

        ret.append ((pos, level, son.text))

    if debug > 1: print ('reading', os.path.basename (fname), len(ret))

  else:

    if 'fname' not in locals ():

      if debug > 0: print ('not found:', os.path.basename (filename))

  return ret





def drawLoc (axes, kiban, level, word, extent = [134, 138, 34, 38],

  alpha=1.0, linewidth=1.0, color='blue', **kwargs):

  codes = []; verts = []

  for pos, lvl, text in kiban:

    if (level is None) or (level >= lvl):

      if (word is None) or (word in text):

        lat = pos[:,0]

        lon = pos[:,1]

        if (extent[0] < max (lon)) and (min (lon) < extent[1])(extent[2] < max (lat)) and (min (lat) < extent[3]):

          codes += [Path.MOVETO]+[Path.LINETO]*(len (pos)-1)

          verts += [(pos[i,1], pos[i,0]) for i in range (len (pos))]

  if len (codes) > 0:

    axes.add_patch (PathPatch (Path (verts, codes), fill=False,

      alpha=alpha, linewidth=linewidth, color=color, **kwargs))



def drawArea (axes, kiban, level, word, extent = [134, 138, 34, 38],

  alpha=1.0, linewidth=1.0, fill=True, edgecolor='blue', facecolor='cyan',

  **kwargs):

  codes = []; verts = []

  for pos, lvl, text in kiban:

    if (level is None) or (level >= lvl):

      if (word is None) or (word in text):

        for p in pos:

          lat = p[:,0]

          lon = p[:,1]

          if (extent[0] < max (lon)) and (min (lon) < extent[1])(extent[2] < max (lat)) and (min (lat) < extent[3]):

            codes += [Path.MOVETO]+[Path.LINETO]*(len (p)-1)

            verts += [(p[i,1], p[i,0]) for i in range (len (p))]

  if len (codes) > 0:

    axes.add_patch (PathPatch (Path (verts, codes), alpha=alpha,

      linewidth=linewidth, fill=fill, edgecolor=edgecolor, facecolor=facecolor,

      **kwargs))