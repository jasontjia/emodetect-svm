-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2024 at 01:40 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `audio`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio_data`
--

CREATE TABLE `audio_data` (
  `id_audio` int(100) NOT NULL,
  `nama_audio` varchar(150) NOT NULL,
  `nada_ori` varchar(150) NOT NULL,
  `intonasi_ori` varchar(199) NOT NULL,
  `volume_ori` varchar(100) NOT NULL,
  `label_manual` varchar(150) NOT NULL,
  `label_otomatis` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `audio_data`
--

INSERT INTO `audio_data` (`id_audio`, `nama_audio`, `nada_ori`, `intonasi_ori`, `volume_ori`, `label_manual`, `label_otomatis`) VALUES
(291, 'ori_uji-tidakmarah1.wav', '1179.902', '4.027', '0.003', 'Tidak Marah', 'Tidak Marah'),
(300, 'ori_uji-tidakmarah2.wav', '1069.376', '4.512', '0.027', 'Tidak Marah', 'Marah'),
(301, 'ori_uji-tidakmarah3.wav', '928.239', '4.336', '0.005', 'Tidak Marah', 'Tidak Marah'),
(302, 'ori_uji-tidakmarah4.wav', '1391.91', '3.93', '0.03', 'Tidak Marah', 'Tidak Marah'),
(303, 'ori_uji-tidakmarah5.wav', '1295.994', '3.89', '0.003', 'Tidak Marah', 'Tidak Marah'),
(304, 'ori_uji-tidakmarah6.wav', '1824.956', '3.765', '0.027', 'Tidak Marah', 'Tidak Marah'),
(305, 'ori_uji-tidakmarah7.wav', '1445.261', '3.555', '0.005', 'Tidak Marah', 'Tidak Marah'),
(306, 'ori_uji-tidakmarah8.wav', '1658.11', '3.657', '0.029', 'Tidak Marah', 'Tidak Marah'),
(307, 'ori_uji-tidakmarah9.wav', '1469.049', '3.832', '0.033', 'Tidak Marah', 'Tidak Marah'),
(308, 'ori_uji-tidakmarah10.wav', '1841.484', '3.476', '0.097', 'Tidak Marah', 'Tidak Marah'),
(309, 'ori_uji-tidakmarah11.wav', '922.815', '4.796', '0.026', 'Tidak Marah', 'Tidak Marah'),
(310, 'ori_uji-tidakmarah12.wav', '1247.799', '3.751', '0.026', 'Tidak Marah', 'Tidak Marah'),
(311, 'ori_uji-tidakmarah13.wav', '1789.806', '3.871', '0.092', 'Tidak Marah', 'Tidak Marah'),
(312, 'ori_uji-tidakmarah14.wav', '1025.636', '5.709', '0.029', 'Tidak Marah', 'Tidak Marah'),
(313, 'ori_uji-tidakmarah15.wav', '1443.284', '4.085', '0.037', 'Tidak Marah', 'Tidak Marah'),
(314, 'ori_uji-tidakmarah16.wav', '1832.019', '3.521', '0.123', 'Tidak Marah', 'Tidak Marah'),
(315, 'ori_uji-tidakmarah17.wav', '1000.089', '4.584', '0.027', 'Tidak Marah', 'Tidak Marah'),
(316, 'ori_uji-tidakmarah18.wav', '1246.606', '4.016', '0.026', 'Tidak Marah', 'Tidak Marah'),
(317, 'ori_uji-tidakmarah19.wav', '1772.922', '3.694', '0.104', 'Tidak Marah', 'Tidak Marah'),
(318, 'ori_uji-tidakmarah20.wav', '451.217', '7.362', '0.025', 'Tidak Marah', 'Tidak Marah'),
(319, 'ori_uji-tidakmarah21.wav', '1625.921', '3.443', '0.01', 'Tidak Marah', 'Tidak Marah'),
(320, 'ori_uji-tidakmarah22.wav', '960.593', '4.685', '0.006', 'Tidak Marah', 'Tidak Marah'),
(321, 'ori_uji-tidakmarah23.wav', '1414.359', '3.627', '0.011', 'Tidak Marah', 'Tidak Marah'),
(322, 'ori_uji-tidakmarah24.wav', '967.14', '5.081', '0.006', 'Tidak Marah', 'Tidak Marah'),
(323, 'ori_uji-tidakmarah25.wav', '1639.249', '3.446', '0.01', 'Tidak Marah', 'Tidak Marah'),
(324, 'ori_uji-tidakmarah26.wav', '982.726', '4.72', '0.006', 'Tidak Marah', 'Tidak Marah'),
(325, 'ori_uji-tidakmarah27.wav', '1636.523', '3.549', '0.012', 'Tidak Marah', 'Tidak Marah'),
(326, 'ori_uji-tidakmarah28.wav', '1131.421', '4.514', '0.008', 'Tidak Marah', 'Marah'),
(327, 'ori_uji-tidakmarah29.wav', '1909.24', '3.742', '0.041', 'Tidak Marah', 'Tidak Marah'),
(328, 'ori_uji-tidakmarah30.wav', '1451.299', '3.905', '0.009', 'Tidak Marah', 'Tidak Marah'),
(329, 'ori_uji-marah41.wav', '1682.429', '3.485', '0.002', 'Marah', 'Tidak Marah'),
(330, 'ori_uji-marah42.wav', '1806.713', '3.459', '0.015', 'Marah', 'Tidak Marah'),
(331, 'ori_uji-marah43.wav', '1580.896', '4.042', '0.003', 'Marah', 'Tidak Marah'),
(332, 'ori_uji-marah44.wav', '1685.496', '3.509', '0.028', 'Marah', 'Marah'),
(333, 'ori_uji-marah45.wav', '1151.816', '4.422', '0.009', 'Marah', 'Tidak Marah'),
(334, 'ori_uji-marah46.wav', '1186.47', '3.817', '0.022', 'Marah', 'Tidak Marah'),
(335, 'ori_uji-marah47.wav', '1649.469', '3.862', '0.006', 'Marah', 'Tidak Marah'),
(336, 'ori_uji-marah48.wav', '1546.635', '3.523', '0.023', 'Marah', 'Marah'),
(337, 'ori_uji-marah49.wav', '1671.734', '3.87', '0.097', 'Marah', 'Marah'),
(338, 'ori_uji-marah50.wav', '1518.427', '3.487', '0.088', 'Marah', 'Marah'),
(339, 'ori_uji-marah51.wav', '929.671', '5.168', '0.038', 'Marah', 'Tidak Marah'),
(340, 'ori_uji-marah52.wav', '1636.675', '3.725', '0.075', 'Marah', 'Tidak Marah'),
(341, 'ori_uji-marah53.wav', '1359.77', '3.648', '0.093', 'Marah', 'Tidak Marah'),
(342, 'ori_uji-marah54.wav', '1208.84', '4.377', '0.082', 'Marah', 'Marah'),
(343, 'ori_uji-marah55.wav', '1347.019', '4.0', '0.102', 'Marah', 'Marah'),
(344, 'ori_uji-marah56.wav', '1585.387', '3.518', '0.095', 'Marah', 'Marah'),
(345, 'ori_uji-marah57.wav', '1203.844', '4.319', '0.079', 'Marah', 'Marah'),
(346, 'ori_uji-marah58.wav', '1435.167', '3.995', '0.095', 'Marah', 'Tidak Marah'),
(347, 'ori_uji-marah59.wav', '1444.765', '3.795', '0.092', 'Marah', 'Tidak Marah'),
(348, 'ori_uji-marah60.wav', '1175.183', '4.226', '0.104', 'Marah', 'Marah'),
(349, 'ori_uji-marah61.wav', '1486.24', '3.616', '0.01', 'Marah', 'Tidak Marah'),
(350, 'ori_uji-marah62.wav', '1082.76', '4.238', '0.009', 'Marah', 'Tidak Marah'),
(351, 'ori_uji-marah63.wav', '1513.174', '3.532', '0.011', 'Marah', 'Marah'),
(352, 'ori_uji-marah64.wav', '961.155', '4.572', '0.012', 'Marah', 'Tidak Marah'),
(353, 'ori_uji-marah65.wav', '1276.305', '3.626', '0.007', 'Marah', 'Tidak Marah'),
(354, 'ori_uji-marah66.wav', '928.808', '4.367', '0.012', 'Marah', 'Tidak Marah'),
(355, 'ori_uji-marah67.wav', '1464.07', '3.56', '0.008', 'Marah', 'Tidak Marah'),
(356, 'ori_uji-marah68.wav', '1007.927', '4.172', '0.015', 'Marah', 'Tidak Marah'),
(357, 'ori_uji-marah69.wav', '1692.926', '3.76', '0.045', 'Marah', 'Marah'),
(361, 'ori_uji-tidakmarah31.wav', '1968.943', '3.598', '0.041', 'Tidak Marah', 'Tidak Marah'),
(362, 'ori_uji-tidakmarah32.wav', '1839.696', '3.82', '0.037', 'Tidak Marah', 'Tidak Marah'),
(363, 'ori_uji-tidakmarah33.wav', '1026.378', '4.357', '0.019', 'Tidak Marah', 'Tidak Marah'),
(365, 'ori_uji-tidakmarah34.wav', '1981.31', '3.606', '0.033', 'Tidak Marah', 'Tidak Marah'),
(366, 'ori_uji-tidakmarah35.wav', '1578.307', '3.6', '0.02', 'Tidak Marah', 'Marah'),
(367, 'ori_uji-tidakmarah36.wav', '1197.859', '4.276', '0.021', 'Tidak Marah', 'Marah'),
(368, 'ori_uji-tidakmarah37.wav', '1968.749', '3.519', '0.048', 'Tidak Marah', 'Tidak Marah'),
(369, 'ori_uji-tidakmarah38.wav', '1640.445', '3.574', '0.043', 'Tidak Marah', 'Tidak Marah'),
(370, 'ori_uji-tidakmarah39.wav', '937.974', '4.74', '0.021', 'Tidak Marah', 'Marah'),
(371, 'ori_uji-tidakmarah40.wav', '2037.698', '3.588', '0.042', 'Tidak Marah', 'Tidak Marah'),
(372, 'ori_uji-marah70.wav', '1443.108', '4.408', '0.099', 'Marah', 'Tidak Marah'),
(373, 'ori_uji-marah71.wav', '1694.672', '3.53', '0.088', 'Marah', 'Marah'),
(374, 'ori_uji-marah72.wav', '1731.177', '3.65', '0.089', 'Marah', 'Marah'),
(375, 'ori_uji-marah73.wav', '1302.149', '4.239', '0.05', 'Marah', 'Tidak Marah'),
(376, 'ori_uji-marah74.wav', '1818.324', '3.452', '0.061', 'Marah', 'Tidak Marah'),
(377, 'ori_uji-marah75.wav', '1428.224', '3.675', '0.038', 'Marah', 'Marah'),
(378, 'ori_uji-marah76.wav', '1206.056', '4.327', '0.068', 'Marah', 'Marah'),
(379, 'ori_uji-marah77.wav', '1808.284', '3.407', '0.085', 'Marah', 'Marah'),
(380, 'ori_uji-marah78.wav', '1513.955', '3.777', '0.068', 'Marah', 'Marah'),
(381, 'ori_uji-marah79.wav', '1272.714', '4.062', '0.152', 'Marah', 'Marah'),
(382, 'ori_uji-marah80.wav', '1715.979', '3.406', '0.061', 'Marah', 'Marah');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio_data`
--
ALTER TABLE `audio_data`
  ADD PRIMARY KEY (`id_audio`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audio_data`
--
ALTER TABLE `audio_data`
  MODIFY `id_audio` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=383;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
